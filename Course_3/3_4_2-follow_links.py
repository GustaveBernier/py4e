from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input('Enter URL: ')
count = int(input("Enter count: "))
pos = int(input("Enter position: "))

def retrieve_next_url(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    href = tags[pos-1].get('href', None)
    return href

for i in range(count+1):    
    print("Retrieving: ", url)
    url = retrieve_next_url(url)