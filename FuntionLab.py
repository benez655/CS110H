'''
Benjamin Day
10/23/2017
Funtion Lab
'''

#Problem 1
def smallest(x, y, z):
    list = [x, y, z]
    a = min(list)
    return a
print('Smallest Interger Problem')
var1 = smallest(int(input('First number?: ')), int(input('Second number?: ')), int(input('Third number?: ')))
print(var1)

def average(x, y, z):
    return (x*y*z)/3
print('Average Of 3 Integers')
var2 = average(int(input('First number?: ')), int(input('Second number?: ')), int(input('Third number?: ')))
print(var2)

#Problem 2
def countVowels(a):
    a = a.lower()
    out = 0
    for i in a:
        if i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u':
            out = out + 1
    return out
print('Vowel Counter')
var3 = countVowels(input('Give me a phrase: '))
print(var3)

#Problem 3
def isLeapYear(x):
    list = []
    for i in range(0, x + 1):
        list.append(i)
    if (len(list) - 1) % 4 == 0:
        return x, 'is a Leap Year'
    else:
        return x, 'is not a Leap Year'
done = False
while not done:
    var4 = isLeapYear(int(input('Give me a year: ')))
    print(var4)
    print('If you want to quit input -1 below, otherwise hit any key to continue')
    quit = input(': ')
    if quit == '-1':
        print('Goodbye')
        done = True
