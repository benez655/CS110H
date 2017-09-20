'''
Benjamin Day
While Loop Handout
9/20/2017
'''

a=int(input('First Number: '))
b=int(input('Second Number: '))
c=int(input('Third Number: '))
d=int(input('Fourth Number: '))

if a==b or a==c or a==d or b==c or b==d or c==d:
    print('There is a pair of numbers')
else:
    print('No pairs')