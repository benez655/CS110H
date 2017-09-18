'''
Benjamin Day
9/18/2017
Quiz 1 q1
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