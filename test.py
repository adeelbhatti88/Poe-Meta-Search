import requests
from bs4 import BeautifulSoup

url = 'https://poe.ninja/api/data/itemoverview?league=Metamorph&type=UniqueWeapon&language=en'

data = requests.get(url)

datajson = data.json()

print(type(datajson))


currency = {}

for val in datajson['lines']:
    currency[val['name']] = val['chaosValue']

print(currency)