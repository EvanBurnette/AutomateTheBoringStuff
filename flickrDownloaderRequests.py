#! python3
# flickrDownloaderRequests.py downloads pictures from flickr based on a keyword search
import requests
import sys, os, bs4

def download(userKeywords):
    os.chdir('/home/evan')

    newDirectoryName = ''
    for keyword in userKeywords:
        newDirectoryName += keyword
        newDirectoryName += '_'
    print(newDirectoryName[:-1])
    #os.mkdir(newDirectoryName[:-1])    #uncomment when ready

    searchString = ''
    for keyword in userKeywords:
        searchString += keyword
        searchString += '%20'
    searchString = searchString[:-3]
    print(searchString)

#TODO Request 'https://www.flickr.com/search/?license=2%2C3%2C4%2C5%2C6%2C9&advanced=1&text=bear%20cub%20panda'
    res = requests.get('https://www.flickr.com/search/?license=2%2C3%2C4%2C5%2C6%2C9&advanced=1&text' + searchString)
    if res.status_code == requests.codes.ok:
        print('OKAY')
        continue
#TODO Request link of first search result

    #TODO In a loop: Download image
    #TODO Request next page using arrow right link

if len(sys.argv) > 1:
    download(sys.argv[1:])
else:
    print('Please enter at least one search term! =)')
