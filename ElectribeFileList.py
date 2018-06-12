textFile = open('ElectribeFileList.txt', 'w')

for number in range(64):
    for letter in 'AbCd':
        textFile.write(letter + str(number + 1) + ',')
    textFile.write('\n')

textFile.close()
