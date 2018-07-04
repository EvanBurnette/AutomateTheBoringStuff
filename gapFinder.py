#! python3
# gapFinder finds gaps in sequences of files and renames files to close gaps

import os, shutil, re

def gapFinder(directory, prefix):
    filePattern = re.compile(prefix + r'(\d{3})(\.txt$)')
    os.chdir(directory)
    fileList = os.listdir()
    print(fileList)
    subList = []
    for item in fileList:
        # If the file matches filepattern search then add it to a subList
        mo = None
        mo = filePattern.search(item)
        if mo is not None:
            subList.append(item)

    subList.sort()

    for i in range(len(subList) - 1):
        # Rename files that are more than +1 above previous file (filegap)
        if (int(filePattern.search(subList[i]).group(1))) != (int(filePattern.search(subList[i+1]).group(1)) - 1):
            newNumber = '%003d' % (int(filePattern.search(subList[i]).group(1)) + 1)
            newName = prefix + newNumber + '.txt'
            shutil.move(os.path.join(directory, subList[i+1]), os.path.join(directory, newName))
            subList[i+1] = newName


gapFinder('/home/evan/Downloads/MyPrograms/AutomateTheBoringStuff/spam/', 'spam')
