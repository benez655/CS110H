'''
Benjamin Day (901815697)
11/13/2017
Set HW
'''

#Q1
color_set = set()                                       # Defines an empty set
color_set.add('Red')                                    # The following lines add 'Red', 'Green', and 'Blue'
color_set.add('Blue')
color_set.add('Green')
print(color_set)

#Q2
for item in color_set:                                  # Iterate through the set and print each element
    print(item)

#Q3
list1 = [1, 3, 6, 78, 35, 55]                           # Defines list1
list2 = [12, 24, 35, 24, 88, 120, 155]                  # Defines list2
set1 = set(list1)                                       # set1 is defined as all the elements in list1
set2 = set(list2)                                       # set2 is defined as all the elements in list2
print(set1 | set2)                                      # Prints the union of the two sets to the console
