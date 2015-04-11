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
        if (letter) in lettersGuessed:
            lettersToGuess.remove(letter)
    
    #nicer formatting a b c d f g 
    for c, letter in enumerate(lettersToGuess):
        lettersToGuess[c] = letter + ' '

    #return as string
    lettersToGuess = ''.join(lettersToGuess)            
    return lettersToGuess
                                                                                                                                       
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getAvailableLetters(lettersGuessed)
# abcdfghjlmnoqtuvwxyz