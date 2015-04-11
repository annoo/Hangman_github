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
            
#test
guessesLeft = 0,
playAgain(guessesLeft)
            