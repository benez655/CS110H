print('Pick a number from 1-20')
print('Yes = 1')
print('No = 0')
print('Is that number divisible by 2?')
x = int(input('Y/N: '))
if x == 1:
    print('Is it prime?')
    x = int(input('Y/N: '))
    if x == 1:
        print('It is 2!')
    if x == 0:
        print('Is is larger than 10?')
        x = int(input('Y/N: '))
        if x == 1:
            print('Is is a multiple of 3?')
            x = int(input('Y/N: '))
            if x == 1:
                print('Is it a multiple of 9?')
                x = int(input('Y/N: '))
                if x == 1:
                    print('It is 18!')
                if x == 0:
                    print('It is 12!')
        if x == 0:
            print('Is it an extreme?')
            x = int(input('Y/N: '))
            if x == 1:
                print('It is 20!')
            if x == 0:
                print('Is it divisible by 7?')
                x = int(input('Y/N: '))
                if x == 1:
                    print('It is 14!')
                if x == 0:
                    print('It is 16!')
if x == 0:
    print('Is it larger than 10?')
    x = int(input('Y/N: '))
    if x == 1:
        print('Is it divisible by 3?')
        x = int(input('Y/N: '))
        if x == 1:
            print('It is 15!')
        if x == 0:
            print('Is it larger than 12?')
            x = int(input('Y/N: '))
            if x == 0:
                print('It is 11!')
            if x == 1:
                print('Is it larger than 15?')
                x = int(input('Y/N: '))
                if x == 0:
                    print('It is 13!')
                if x == 1:
                    print('Is it larger than 18?')
                    x = int(input('Y/N: '))
                    if x == 1:
                        print('It is 19!')
                    if x == 0:
                        print('It is 17!')
