'''
Benjamin Day - 901815697
10/30/2017
Test 3
'''

list = []
for i in range(0, 3):
    entry = []
    iD = input('Student ID: ')
    entry.append(iD)
    name = input('Student Name: ')
    entry.append(name)
    mark = int(input('Student Grade: '))
    entry.append(mark)
    list.append(entry)
print(list[0][1], 'scored', list[0][2], '% on the first exam')
print(list[1][1], 'scored', list[1][2], '% on the first exam')
print(list[2][1], 'scored', list[2][2], '% on the exam')
x = 0
for j in list:
    x = x + j[2]
print('The average score of the class is', round(x/len(list), ), '%')
grades = []
for k in list:
    grades.append(k[2])
print('The highest mark obtained is', max(grades), '%')
print('The lowest mark obtained is', min(grades), '%')
