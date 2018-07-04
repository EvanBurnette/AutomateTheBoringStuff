#! python3

import os, re, pprint
import requests

import sys
import codecs

os.chdir('/home/evan/Downloads/MyPrograms/')
newDir = 'bear'
if os.path.isdir(newDir) == False:
    os.mkdir(newDir)
os.chdir(newDir)

page = requests.get('http://www.flickr.com/search/?text=bear').text

#find all jpg links
jpgRe = re.compile('''c1.staticflickr.com.*jpg''', re.UNICODE)
linkList = jpgRe.findall(page, re.UNICODE)
print(len(linkList))
for item in linkList:
    print(item)

for link in linkList:
    image = requests.get('http:' + link)
    imgfile = open(os.basename(link), 'wb')
    for chunk in image.iter_contents(100000):
        file.write(chunk)
