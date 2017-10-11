empty = ''
string = input('Enter phrase: ')

for n in string:
    empty = n + empty
print(string)
print(empty)