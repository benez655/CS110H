for row in range(0,8):
    if row%2==0:
        for col in range(0,8):
            if col%2==0:
                print('x', end='')
            else:
                print('_', end='')
    else:
        for col in range(0,8):
            if col%2!=0:
                print('x', end='')
            else:
                print('_', end='')
    print()