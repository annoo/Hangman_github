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

#test
secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'l', 's']
print getGuessedWord(secretWord, lettersGuessed)