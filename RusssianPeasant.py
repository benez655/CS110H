'''
Benjamin Day
8/30/2017
Russian Peasant Mutiplication
'''

#input two multiplicands into 'A' and 'B', 'mySum' is the total
A=int(input('First Multiplicand = '))
B=int(input('Second Multiplicand =  '))
mySum=0
Z=A
Y=B
#while A is larger than one divide it by 2 (removing remainders)
while A>1:
    A=A//2
#check to see if the value in A is even by seeing if there is a remainder after dividing by 2
 #if theres is no remainder, double B, else double B and add it to the total 'mySum'
    if (A%2)==0:
        B=B*2
    else:
        B=B*2
        mySum=B+mySum
print(Z,'*', Y, '=', mySum)