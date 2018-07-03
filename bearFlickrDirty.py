#! python3

import os, re, pprint
import requests

import sys
import codecs

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
#sys.stderr = codecs.getwriter('utf8')(sys.stderr)

os.chdir('/home/evan/Downloads/MyPrograms/')
newDir = 'bear'
if os.path.isdir(newDir) == False:
    os.mkdir(newDir)
os.chdir(newDir)

page = requests.get('http://www.flickr.com/search/?text=bear').text

#find all jpg links
jpgRe = re.compile('''c1.staticflickr.com.*jpg''', re.UNICODE)
linkList = jpgRe.findall(page, re.UNICODE)

for link in linkList:
    image = requests.get('http://' + link)
    imgFile = open(os.path.basename(link), 'wb')
    for chunk in image.iter_content(100000):
        imgFile.write(chunk)
