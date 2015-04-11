variables:
helpfucntions: getavailable letters, iswordguessed,getguessedword, feedback, playAgain

start game

guess while guesses left > 0
    # check valid guess
      #  no: print no good and restart
       # yes:
        check letter already guessed 
            yes:    print you already guessed that letter. guess again
                    feedback on guess: available letters + word so far
                    reguess ---> back to line 3
            no: check if letter is in word
                    yes:    print good guess
                            into guessed letter list
                            check if word is guessed
                                yes:    congratulations!
                                        play again?
                                            yes: ---> goto line 1
                                            no: print goodbye (=end)
                                no: feedback on guess: available letters 
                                    + (update!) word so far
                                    another guess ---> goto line 3
                    no: print oops, not in word
                        into guessed letter list
                        guessesLeft -=
                        feedback on guess: (update!) availabe letters
                                            + word so far
print sorry you ran out of guesses 
print the word I had in mind was word (red?)          