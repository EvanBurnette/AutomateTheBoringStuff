import os, re, shutil

def consolidate(folderAbsolutePath):
    os.chdir(folderAbsolutePath)
    number = 2
    newFolder = 'Images'

    # Make a new folder to move images to
    if os.path.exists(newFolder):
        while True:
            if os.path.exists(newFolder + str(number)):
                number += 1
            else:
                newFolder = newFolder + str(number)
                break

    os.mkdir(newFolder)

    imgExt = re.compile('.+\\.jpg$|.+\\.png$|.+\\.bmp$')

    for folderName, subfolders, filenames in os.walk(folderAbsolutePath):
        # Find all image files
        for filename in filenames:
            if imgExt.search(filename) is not None:
                # Move image file to newFolder
                # shutil.move(filename, newFolder) # uncomment after practice run
                # Print out each move made
                print('Moving %s to %s' % (filename, newFolder))

    return('\nDone\n')

consolidate(input('Enter an absolute path to a directory to consolidate image files: \n'))
