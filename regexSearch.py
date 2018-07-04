#! python3
import os
import re
import pprint

# Identify .txt files in a directory
textFileList = []
userDir = input("Enter a directory to search for text files: ")
if userDir != '':
    os.chdir(userDir)
for file in os.listdir():
    if file.endswith('.txt'):
        textFileList.append(file)

# TODO: Open each file and return matching patterns for a user input regex
userRe = input('Enter a regular expression to search for: ')
userRe = re.compile(userRe)

for file in textFileList:
    readFile = open(file, 'r')
    readFile = readFile.read()
    print('Filename: ' + file + '   Matches: ', end='')
    pprint.pprint(userRe.findall(readFile))

# Print results to the screen
