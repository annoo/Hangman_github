def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # if all letters of apple are in listletterg, then the wordguessed is true
    
    i = 0
    for letter in secretWord:
        if letter not in lettersGuessed:
            i += 1
    return not (i > 0)
    
secretWord = 'pears'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print isWordGuessed(secretWord, lettersGuessed)