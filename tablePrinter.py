#! python3
"""TablePrinter.py takes a list of lists of strings and displays it in
right justified columns."""


def maxWordLength(wordList):
    longestWord = 0
    for i in range(len(wordList)):
        wordLength = len(wordList[i])
        if wordLength > longestWord:
            longestWord = wordLength
    return longestWord


def printTable(table):
    lengthList = []
    tableLength = len(table)
    listLength = len(table[0])
    for i in range(0, len(table)):
        lengthList.append(maxWordLength(table[i]))
    for k in range(listLength):
        for j in range(0, tableLength):
            print(table[j][k].rjust(lengthList[j]), end='')
            print(' ', end='')
        print(' ')
    return


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
