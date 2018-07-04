#! python3
# MadLibs.py replaces capitalized parts of speech with user input words

import os
import re

os.chdir(r'/home/evan/Downloads/MyPrograms/AutomateTheBoringStuff/')
# change to correct path

madFile = open('madBlanks.txt')

madString = madFile.read()

madString = madString.split()

caps = re.compile(r'ADJECTIVE|NOUN|VERB|ADVERB')

for i in range(len(madString)):
    if caps.findall(madString[i]) != []:
        blankType = caps.search(madString[i]).group()
        madString[i] = caps.sub(input('Enter a ' + blankType.lower() + ': '),
                                madString[i])

madString = " ".join(madString)

print('\n\n' + madString + '\n\n')
