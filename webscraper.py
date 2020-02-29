import requests
from bs4 import BeautifulSoup

data = requests.get('https://poe.watch/prices?category=currency&league=Metamorph')

soup = BeautifulSoup(data.content, 'html.parser')
soup.prettify()
print(soup.find_all('tbody')[0].find_all('tr'))
