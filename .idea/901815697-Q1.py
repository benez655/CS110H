'''
Benjamin Day
9/18/2017
Quiz 1
'''

'''
Q1
'''

#input 3 values and assign them to 'A','B', and 'C'
A=float(input('First Number: '))
B=float(input('Second Number: '))
C=float(input('Third Number: '))

#check if the numbers are in increasing order and if so print 'the numbers are in increasing order'
if A<B<C:
    print('the numbers are in increasing order')
#check if the numbers are in decreasing order and if so print 'the numbers are in decreasing order'
elif A>B>C:
    print('the numbers are in decreasing order')
#otherwise print that the numbers are random
else:
    print('the numbers are in a random order')




'''
Q2
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