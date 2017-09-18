'''
Benjamin Day
9/18/2017
Quiz 1
'''

A=float(input('First Number: '))
B=float(input('Second Number: '))
C=float(input('Third Number: '))

if A<B<C:
    print('the numbers are in increasing order')
elif A>B>C:
    print('the numbers are in decreasing order')
else:
    print('the numbers are in a random order')