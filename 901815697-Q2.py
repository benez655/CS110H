'''
Benjamin Day
10/11/2017
Exam 2 - Q1
'''
from random import randint                                                              #imports randint function

done = False
while not done:
    print('1: Play?')                                                                   #menu options
    print('2: Exit')
    var = int(input('Selection: '))

    if var == 1:                                                                        #option 1: the guessing game
        a = str(randint(0, 10))                                                         # assigns random int to variable 'a'
        g = 3                                                                           #three guesses
        print('I have picked a random number between 0 and 10, what is it?')
        print(g, 'chance(s)')
        while g > 0:                                                                    #while the user still has guesses, run the nested code
            x = input(': ')                                                             #user inputs a number
            if x.isdigit():                                                             #checks to make sure a number is inputed
                if x != a:
                    g = g - 1                                                           #checks to see if the guess and number are equal
                    print('Incorrect,', g, 'chance(s) left')                            #if not, takes a guess away and asks again for an input
                if x == a:
                    print('You Win!')                                                   #if they do equal prints 'You win'
                    g = -1
            else:
                print('Not a number, try again')
        if g == 0:                                                                       #user has run out of guesses, g = 0
            print('You Lose!')                                                           #and is given the option to start over or exit

    if var == 2:
        done = True                                                                     #option 2: exits game
        print('Thanks for playing')
