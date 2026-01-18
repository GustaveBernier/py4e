from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter - ')
html = urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
count= 0
total = 0
for tag in tags:
    count = count + 1
    total = total + int(tag.contents[0])

print("Count", count)
print("Sum", total)