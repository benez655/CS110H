'''
Benjamin Day (901815697)
11/06/2017
File Practice
'''

#Q1
file = open('c:/FilePractice/myfile.txt', 'r')         # Call file myfile.txt
for line in file:
    line = line.strip().split()                        # Take each line and clean it and split each line by
    for n in range(0, len(line)):                      # words and add them to a list
        word = line[n].strip(',.?!')                   # Each word in the list 'line' remove punctuation
        if line[n] == line[-1]:                        # Check to see if the element is the last one in
            print(word, end='.')                       # the list and if it is print '.', else print ' '
        else:
            print(word, end=' ')
    print()
file.close()

#Q2
file = open('c:/FilePractice/hello.txt', 'r')          # Call file hello.text
for line in file:
    line = line.strip()                                # Clean each line and leave the sting
    reverse = ''                                       # Create an empty string variable
    for n in line:
        reverse = n + reverse                          # Adds each part of the line to the empty string
    print(reverse)
file.close()

#Q3
input = open('c:/FilePractice/input.txt', 'r')         # Call file input.txt
output = open('c:/FilePractice/output.txt', 'r+')      # Call file output.txt in writable mode
list = []                                              # Creates empty List
for line in input:
    line = line.strip()                                # Cleans each line from input.txt
    list.append(line)                                  # Adds the clean string to the empty list
for n in range(-1, (-len(list) - 1), -1):              # Iterates through the list backwards starting with last element
    output.write(list[n] + '\n')                       # Writes each element to output.txt and adds newline
    print('Writing to file')
input.close()
output.close()
