# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:\Users\Ann\Documents\priveAnn\Py_scripts\hangman\words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


#check if word if found
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i = 0
    for letter in secretWord:
        if letter not in lettersGuessed:
            i += 1
    return not (i > 0)

#gives image of word so far guessed
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

#feedback
def feedback(getGuessedWord, getAvailableLetters, lettersGuessed, guessesLeft):
    '''
    input: function getGuessedWord
           function getAvailableletters
           lettersGuessed
           guessesLeft
    gives you feedback on 3 domains: 
    - word so far 
    - letters not yet guessed 
    - how many guesses left    
    ouput: several lines of printed text       
    '''                     
    print''
    
    #word so far
    print "Your word so far looks like this:"
    print getGuessedWord(secretWord, lettersGuessed)
    
    #letters that are not yet guessed
    print "These choices are open:"
    print getAvailableLetters(lettersGuessed)
    
    #available guesses
    print "You have %i guesses left." % guessesLeft 
    
    print "____________________________________________________"  

#Would you like to play again?
def playAgain(guessesLeft):
    '''
    input: non
    asks the player to play again
    returns guessesLeft to 8 if 'y' is pressed
    '''
    
    clearAnswer = False
    
    while clearAnswer == False:
        again = raw_input('Would you like to play again? y or n \n')
        again = again.lower()
       
        if again == 'n':  
            clearAnswer == True
            print 'Goodbye! Thank you for playing.'
            return guessesLeft
        elif again == 'y':
            print "Let's pick a new word..."
            clearAnswer == True
            guessesLeft = 8
            return guessesLeft
        else:
            print "I did'nt get that."
            clearAnswer == False
            
#the Game
#--------
def hangman(secretWord, guessesLeft, lettersGuessed):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    #start the game
    print "Welcome to the game, Hangman!"
    print "I'm thinking of a word that has %i letters" % len(secretWord)
    print "You have %i guesses in total." % guessesLeft
    print "You can guess one letter per round."   
        
    while guessesLeft > 0: 

        guess = raw_input('What is your guess? ')
        #making sure both lower and upper cases are accepted
        guess = guess.lower()
        
        #check if guess is a valid guess
        
        #check if you've already made this guess
        if guess in lettersGuessed:
            print "You've already guessed that letter."
            print "Make another choice."
            feedback(getGuessedWord, getAvailableLetters, lettersGuessed, guessesLeft)
            return guessesLeft
            #if you have guessed this letter: you can try again in while loop
            #if you haven't guessed this letter yet = continue the loop in else
            
        else:    
            #check if letter is in word
            if guess in secretWord:
                #every valid guessed letter goes into the lettersGuessed list
                lettersGuessed.append(guess)
                print "Good guess! Your letter is in my word."
                                                                            
                #check if this was the final letter
                if isWordGuessed(secretWord, lettersGuessed) == True:
                    print "Congratulations!"
                    print "You've guessed my word %s" % secretWord
                    playAgain(guessesLeft) 
                    #if you did not guess the secret word, you get feedback
                
                else:
                    feedback(getGuessedWord, getAvailableLetters, lettersGuessed, guessesLeft) 
                    #it will loop back to the while-statement
                    #so you can guess again                                    
            
            else: #if gues is not in secretWord
                #every valid guessed letter goes into the lettersGuessed list
                lettersGuessed.append(guess)
                print "Sorry, this letter is not in my word."
                guessesLeft -=1 
                feedback(getGuessedWord, getAvailableLetters, lettersGuessed, guessesLeft) 
                #it will loop back to the while-statement with -1 guess
                #so you can guess again 
    
    #if you have no more guesses left              
    print "Sorry you ran out of guesses."
    print "The word I had in mind was %s" % secretWord
    playAgain(guessesLeft)

#-----------------------------------------------------------
#end of definitions

# variables
lettersGuessed = []
guessesLeft = 8        
secretWord = chooseWord(wordlist).lower()

# let's play!
hangman(secretWord, guessesLeft, lettersGuessed)