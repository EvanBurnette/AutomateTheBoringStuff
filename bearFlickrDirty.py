#! python3

import os, re, pprint
import requests

print(os.getcwd())

page = open('flickrtest.html')



#find all jpg links
jpgRe = re.compile('c1.staticflickr.com.*jpg', re.UNICODE)
linkList = jpgRe.findall(page.read().decode('utf-8'), re.UNICODE)
print(len(linkList))
pprint.pprint(linkList)
page.close()

for link in linkList:
    image = requests.get('http:' + link)
    imgfile = open(os.basename(link), 'wb')
    for chunk in image.iter_contents(100000):
        file.write(chunk)
