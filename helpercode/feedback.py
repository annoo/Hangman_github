def feedback(getGuessedWord, getAvailableLetters, lettersGuessed, guessesLeft):
    #feedback on guess
    
    #word so far
    print "Your word so far looks like this:"
    print getGuessedWord(secretWord, lettersGuessed)
    
    #letters that are not yet guessed
    print "These choices are open:"
    print getAvailableLetters(lettersGuessed)
    
    #available guesses
    print "You have %i guesses left." % guessesLeft
#___________________________________________________________________
# to test code: helpfunctions

#gives image of word so far guessed
#----------------------------------
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wordGuessed = list('_' * len(secretWord))

    for count, letter in enumerate(secretWord):
        if letter in lettersGuessed:
            wordGuessed[count] = letter

    wordGuessed = ''.join(wordGuessed)

    return wordGuessed

#gives all the letters of the alfabeth, exluding the ones you've guessed
#------------------------------------------------------------------------
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #start out with whole alphabet 
    # ! but this is already done on higher level 
    #-> better to do it higher level once or each time in def?
    # then ascii_lowercase => string.ascii_lowercase
    from string import ascii_lowercase
    
    #make a mutable list from unmutable string
    lettersToGuess = list(ascii_lowercase)
    
    #copy list so we can iterate over it...    
    lettersToGuess1 = lettersToGuess[:]
 
    #remove already guessed letters from alphabet list   
    for c, letter in enumerate(lettersToGuess1):
        if (letter or (letter + ' ')) in lettersGuessed:
            lettersToGuess.remove(letter)
    
    #nicer formatting a b c d f g 
    for c, letter in enumerate(lettersToGuess):
        lettersToGuess[c] = letter + ' '

    #return as string
    lettersToGuess = ''.join(lettersToGuess)            
    return lettersToGuess

#test
secretWord = 'worldview'
lettersGuessed = ['b', 'p', 'e', 'o', 'c', 'f']
guessesLeft = 3
feedback(getGuessedWord, getAvailableLetters, lettersGuessed, guessesLeft)
