'''
Benjamin Day (901815697)
11/15/2017
Dictionaries Lab
'''
input = open('c:/FilePractice/Densities.txt', 'r')              # Opens file to work with
densities = {}                                                  # Creates empty dictionary
for line in input:                                              # Iterates through each line in the file
    line = line.rstrip()                                        # Clears new line character
    words = line.split()                                        # Splits the line by words
    substance = words[0]                                        # Defines 'substance' as the first word in the line
    density = words[1]                                          # Defines 'density' as the second word in the same line
    densities[substance] = density                              # Adds Key:Value pairs substance:density in dictionary
input.close()                                                   # Closes input file
for key in sorted(densities):                                   # Prints each Key:Value pair to console in sorted order
    print(key, densities[key])
