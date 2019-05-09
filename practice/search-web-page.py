import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, features="html.parser")
titles = soup.find_all("h2")

for t in titles:    
    c = t.findChild('span')
    if c:
        print(c.text)