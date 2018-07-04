#! python3
# flickrFinDL takes command line args and
# downloads the top 100 matching images from flickr.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import os
import requests
import time

os.chdir('C:\\Users\\EvanB\\Documents\\MyPrograms\\')

if len(sys.argv) > 1:
    searchString = 'https://www.flickr.com/search/?license=4%2C5%2C9%2C10&advanced=1&dimension_search_mode=min&height=640&width=640&text=' + '%20'.join(sys.argv[1:]) + '&media=photos'
    newDir = '_'.join(sys.argv[1:])
else:
    searchString = 'https://www.flickr.com/search/?text=bear&license=4%2C5%2C9%2C10&media=photos'
    newDir = 'bear'
if (os.path.isdir(newDir) == False):
    os.makedirs(newDir, exist_ok=True)
os.chdir(newDir)
print(os.getcwd())
browser = webdriver.Chrome()
print('Opening ' + searchString)
browser.get(searchString)

def findImageLink():
    image = browser.find_element_by_id('allsizes-photo')
    imageLink = image.find_element_by_xpath('.//img')
    return(str(imageLink.get_attribute('src')))

def nextPage():
    body = browser.find_element_by_tag_name('body')
    body.send_keys(Keys.RIGHT)
    return

time.sleep(5)
picElems = browser.find_elements_by_class_name('photo-list-photo-view')

picLen = len(picElems)
print('picLen = ' + str(picLen))
if picLen > 100:
    picLen = 100
if picLen > 1:
    picElems[0].click()
    savedPics = 0;
    while savedPics < picLen:
        time.sleep(1)
        try:
            dlIcon = browser.find_element_by_class_name('ui-icon-download')
        except:
            nextPage()
            print('Skipping Ad')
            continue
        dlIcon.click()
        time.sleep(1)
        vas = browser.find_element_by_link_text('View all sizes')
        vas.click()
        time.sleep(1)
        imgLink = findImageLink()
        print('Downloading image ' + str(1+savedPics) + ' ' + imgLink)
        res = requests.get(imgLink)
        res.raise_for_status()
        fileName = imgLink.split('/')[-1]
        print(fileName)
        imageFile = open(fileName, 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
        savedPics += 1
        browser.back()
        time.sleep(1)
        nextPage()


browser.quit()
