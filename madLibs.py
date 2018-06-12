#! python3
# MadLibs.py replaces capitalized parts of speech with user input words

import os

os.chdir('C:\\Users\\EvanB\\Documents\\MyPrograms\\AutomateTheBoringStuff')#change to correct path

madFile = open('.\\madBlanks.txt')

madString = madFile.read()

madString = madString.split()

for i in range(len(madString)):
    if madString[i].startswith('ADJECTIVE'):
        madString[i] = input('Enter an adjective:')
    elif madString[i].startswith('NOUN'):
        madString[i] = input('Enter a noun:')
    elif madString[i].startswith('VERB'):
        madString[i] = input('Enter a verb:')
    elif madString[i].startswith('ADVERB'):
        madString[i] = input('Enter an adverb:')

madString = " ".join(madString)

print('\n\n' + madString + '\n\n')
