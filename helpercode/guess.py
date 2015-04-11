def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    #start out with whole alphabet 
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
    
def feedback(getGuessedWord, getAvailableLetters, guessesLeft):
    #feedback on guess
    
    #word so far
    print "Your word so far looks like this:"
    print getGuessedWord(secretWord, lettersGuessed)
    
    #letters that are not yet guessed
    print "These choices are open:"
    print getAvailableLetters(lettersGuessed)
    
    #available guesses
    print "You have %i guesses left." % guessesLeft

def guess(guessesLeft, secretWord, lettersGuessed):
    '''
    input:guessesLeft
    
    loops through the guessing game as long as you have guesses left
    
    returns nothing
    '''    

    while guessesLeft > 0: 

        yourGuess = raw_input('What is your guess? ')
        #making sure both lower and upper cases are accepted
        yourGuess = yourGuess.lower
        #every guessed letter goes into the lettersGuessed list
        lettersGuessed.append(yourGuess)#check if letters is already guessed
        
        #check if guess is a valid guess
        if yourGuess in lettersGuessed:
            print "You've already guessed that letter."
            print "Make another choice."
            feedback(getGuessedWord, getAvailableLetters, guessesLeft)    
            #if you haven't guessed this letter yet = continue the loop
            
            #check if letter is in word
            if yourGuess in secretWord:
                print "Your letter is in the word."
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print "Congratulations!"
                    print "You've guessed my word %s" % secretWord
                    playAgain() 
                    #(else=) if you did not guess the secret word, 
                    #it will loop back to the while-statement
                    #so you can guess again                                                         
            else:
                print "sorry, this letter is not in my word."
                guessesLeft =-1 
                feedback(getGuessedWord, getAvailableLetters, guessesLeft) 
                #it will loop back to the while-statement
                #so you can guess again 
    
    #if you have no more guesses left              
    print "Sorry you ran out of guesses."
    print "The word I had in mind was %s" % secretWord

#test
guessesLeft = 8
secretWord = 'apple'
lettersGuessed = []
guess(guessesLeft, secretWord, lettersGuessed)
            
