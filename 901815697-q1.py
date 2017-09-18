'''
Benjamin Day
9/18/2017
Quiz 1 q2
'''

#assign a desired value to 'A'
A=int(input('Give me a number between 1 and 12: '))

if A>=1 and A<=12:                                  #check to see if the input value is between 1 and 12
    if A==1:
        print('That is January')
    elif A==2:
        print('That is February')
    elif A==3:
        print('That is March')
    elif A==4:
        print('That is April')
    elif A==5:
        print('That is May')
    elif A==6:                                        #checks the value of 'A' and prints corresponding month
        print('That is June')
    elif A==7:
        print('That is July')
    elif A==8:
        print('That is August')
    elif A==9:
        print('That is September')
    elif A==10:
        print('That is October')
    elif A==11:
        print('That is November')
    elif A==12:
        print('That is December')
else:                                     #if the number is outtside the range between 1 nad 12 then prints a response to the user
    print('I said BETWEEN 1 and 12!')
