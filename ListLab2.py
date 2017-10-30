'''
Benjamin Day
10/18/2017
List Lab 2
'''

#Q1

print('Q1:')
a = []
for i in range(5):
    num = int(input('Number: '))
    a.append(num)
print('Your list is:', a)
print(sum(a))
mult = 1
for i in range(len(a)):
    mult = mult * a[i]
print(mult)
print(max(a))
print()


#Q2

print('Q2:')
b = ['ab', 'Helloh', 'abab', 'abA', '1221', '2321', 'yellow']
out = []
for i in b:
    i = i.lower()
    if len(i) >= 3 and i[0] == i[len(i) - 1]:
        out.append(i)
print('There are', len(out), 'elements that satisfy the constraints')