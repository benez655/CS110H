#Benjamin Day
#9/13/2017
#Homework 2

#give your income for the year
income=float(input('How much did you make this year?: '))

#income tax for those who made 50,000 or less
if income<=50000:
    tax=income*0.01
#income tax for those who made between 50,000 and 75,000
elif income<=75000:
    tax=(50000*0.01)+((income-50000)*0.02)
#income tax for those who made between 75,000 and 100,000
elif income<=100000:
    tax=(50000*0.01)+(25000*0.02)+((income-75000)*0.03)
#income tax for those who made between 100,000 and 250,000
elif income<=250000:
    tax=(50000*0.01)+(25000*0.02)+(25000*0.03)+((income-100000)*0.04)
#income tax for those who made between 250,000 and 500,000
elif income<=500000:
    tax=(50000*0.01)+(25000*0.02)+(25000*0.03)+(50000*0.04)+((income-250000)*0.05)
#income tax for those who made over 500,000
elif income>500000:
    tax=(50000*0.01)+(25000*0.02)+(25000*0.03)+(50000*0.04)+(50000*0.05)+((income-500000)*0.06)

print('$%.2f'%tax)