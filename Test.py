
done=False
while not done:
    print('1 - Option 1')
    print('2 - Option 2')
    print('3 - Exit')
    print('')
    answer=int(input('Select an option please: '))
    if answer==1:
        print('')
        print('A')
    elif answer==2:
        print('')
        print('B')
    elif answer==3:
        done=True
        print('')
        print('Goodbye')
    else:
        print('Try again')