#! python3
# soupTest.py tests out behavior of beautiful soup

import requests, bs4, os
print(os.getcwd())

res = requests.get('http://www.flickr.com/search/?text=bear')
res.raise_for_status()
file = open('flickrtest.html', 'wb')
for chunk in res.iter_content(100000):
    file.write(chunk)

soup = bs4.BeautifulSoup(res.text, 'html5lib')
elems = soup.select('.photo-list-photo-view')
s = soup.text.encode('utf8')
print()

print(len(elems))
