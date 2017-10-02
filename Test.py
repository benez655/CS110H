var = input('Continue(Y/N): ')

if var.lower().endswith('y'):
    digit = input('What number do you want to double?: ')
    if digit.isdigit:
        answer = digit*2
        print(answer)
    else:
        print('Error')
elif var.lower().endswith('n'):
    print('Exit')
else:
    print('Error')