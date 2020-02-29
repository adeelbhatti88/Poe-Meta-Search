
import requests

uniqueArmourDataUrl = "https://poe.ninja/api/data/itemoverview?league=Metamorph&type=UniqueArmour&language=en"

uniqueArmourData = requests.get(uniqueArmourDataUrl)
uniqueArmourDataJson = uniqueArmourData.json()
uniqueArmourDic = {}
for val in uniqueArmourDataJson['lines']:
    uniqueArmourDic[val['name']] = val['chaosValue']

print(uniqueArmourDic)


# #getting currency sell prices.
# url = 'https://poe.ninja/api/data/currencyoverview?league=Metamorph&type=Currency&language=en'
#
# data = requests.get(url)
#
# datajson = data.json()
#
# currency = {}
#
# #this will be usefull for calculating if a item is profitable to sell or not.
# for val in datajson['lines']:
#     currency[val['currencyTypeName']] = val['chaosEquivalent']
#
# print(currency)


# #unique weapons
# url = 'https://poe.ninja/api/data/itemoverview?league=Metamorph&type=UniqueWeapon&language=en'
#
# data = requests.get(url)
#
# datajson = data.json()
#
# print(type(datajson))
#
#
# currency = {}
#
# for val in datajson['lines']:
#     currency[val['name']] = val['chaosValue']
#
# print(currency)