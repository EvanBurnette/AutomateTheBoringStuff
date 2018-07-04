#! python3
# findLargeFiles.py walks a directory tree to identify files larger than 100MB.
import os, math

def big(topFolder):
    os.chdir(topFolder)
    absWorkingDir = os.path.abspath('.')
    for foldername, subfolders, filenames in os.walk(topFolder):
        for filename in filenames:
            absPath = os.path.abspath(filename)
            filesize = os.path.getsize(os.path.join(foldername, filename)) / 1000000 #1000000 bytes per MB
            if filesize > 10:
                print(absPath + ' is ' + str(int(math.floor(filesize))) + ' MB')
    return

big('/home/evan/Downloads')
