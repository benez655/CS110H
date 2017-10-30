'''
Benjamin Day
While Loop Handout
9/20/2017
'''

done=False
while not done:
    print('1 - Pairs Program')
    print('2 - Even Sum')
    print('3 - Squares Sum')
    print('4 - Exit')
    answer=int(input('What is your selection: '))

    if answer==1:
        'Write a program to identify the number of pairs in 4 numbers'
        pair=0
        a=int(input('First Number: '))
        b=int(input('Second Number: '))
        c=int(input('Third Number: '))
        d=int(input('Fourth Number: '))

        if a==b or a==c or a==d:
            pair=1
        elif b==c or b==d:
            pair=1
        elif c==d:
            pair=1
        if (a==b and c==d) or (a==c and b==d) or (a==d and b==c):
            pair=2
        print('')
        print('There are',pair,'pair(s)')
        print('')

    if answer==2:
        'copmute the sum of all even integers between 1 and 100'
        a=100
        mySum=0
        while a>1:
            if (a%2)==0:
                mySum=mySum+a
                a=a-1
                total=mySum
            else:
                a=a-1
        print('')
        print('the sum of all even integers between 100 and 1 is:',total)
        print('')

    if answer==3:
        'compute the sum of the squares of the numbers between 1 and 15'
        a=1
        mySum=0
        while a<16:
            mySum=mySum+(a*a)
            a=a+1
            total=mySum
        print('')
        print('The sum of the squares of the numbers between 1 and 15 is:',total)
        print('')

    if answer==4:
        print(' ')
        print('Goodbye')
        done=True