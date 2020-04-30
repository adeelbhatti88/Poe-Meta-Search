import requests
import tkinter as tk
import operator
import math
from PIL import Image, ImageTk

def exalt_Ratio_Window():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)

    # add a button
    button = tk.Button(root,text="Calculate Ratio", font=1, command=lambda: calculate_Exalt_Ratio(entry.get(), label))
    button.place(x = 130, y = 100, height = 50)

    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)



def calculate_Exalt_Ratio(entry, label):
    exaltedOrbPrice = currency.get("Exalted Orb")
    exaltedOrbRatio = float(exaltedOrbPrice) * float(entry)
    chaosOrbs = " Chaos Orbs"
    label['text'] = str(round(exaltedOrbRatio)) + chaosOrbs

#Divination Cards search window
def main_window10():
    root = tk.Toplevel()
    root.title("Divination Card Search")
    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)
    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Div_Cards_Value(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Div Card", font=1, command=lambda: top_Div_Card_Item(entry.get(), label))
    button2.place(x=240, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an div card to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)

#Unique Acessories search window
def main_window9():
    root = tk.Toplevel()
    root.title("Unique Acessories Search")
    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)
    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_unique_acessories_Value(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Acessory", font=1, command=lambda: top_Unique_Accessories_Item(entry.get(), label))
    button2.place(x=240, y=100, height = 50)

    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an item to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


#fossil search window
def main_window8():
    root = tk.Toplevel()
    root.title("Fossil Search")
    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)
    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_fossilValue(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Fossil", font=1, command=lambda: top_Fossil_Item(entry.get(), label))
    button2.place(x=264, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an fossil to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)



#scarab search window
def main_window7():
    root = tk.Toplevel()
    root.title("Scarab Search")
    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_scarabValue(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Scarab", font=1, command=lambda: top_Scarab_Item(entry.get(), label))
    button2.place(x=254, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an scarab to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)
#incubator Window
def main_window6():
    root = tk.Toplevel()
    root.title("Incubator Search")
    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_incubatorValue(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Incubator", font=1, command=lambda: top_Incubator_Item(entry.get(), label))
    button2.place(x=240, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an incubator to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)
#uniqueJewels window
def main_window5():
    root = tk.Toplevel()
    root.title("Unique Jewels Search")

    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_uniqueJewelValue(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Unique Jewel", font=1, command=lambda: top_Unique_Jewel_Item(entry.get(), label))
    button2.place(x=200, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an unique Jewel to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


#unique armour six link armour window
def main_window4():
    root = tk.Toplevel()
    root.title("Unique Armour (Six-Link) Search")

    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Unique_Armour_Six_Lilnk_Value(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top 6-Link Armour", font=1, command=lambda: top_6LinkArmour_Item(entry.get(), label))
    button2.place(x=195, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an item to Search for.."
    # label2 = tk.Label(root, font = 200, bg="white")
    # label2.place(x=45, y = 25)
    # label2['text'] = "Results will be value of 1-4 linked armours only"



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)

#unique armour window
def main_window3():
    root = tk.Toplevel()
    root.title("Unique Armour (1-4) links Search")

    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Unique_Armour_Value(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Armour", font=1, command=lambda: top_Armour_Item(entry.get(), label))
    button2.place(x=240, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an item to Search for.."






    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


#weapon window
def main_window2():
    root = tk.Toplevel()
    root.title("Unique Weapon Search")

    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_weaponValue(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Weapon", font=1, command=lambda: top_Weapon_Item(entry.get(), label))
    button2.place(x=240, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an item to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)



#currency window
def main_window1():
    root = tk.Toplevel()

    root.title("Currency Search")
    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 25, y = 50, width = 350, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_value(entry.get(), label))
    button.place(x = 25, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Currency", font=1, command=lambda: top_Currency_Item(entry.get(), label))
    button2.place(x=240, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Please Enter an  Item to Search for.."



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


def aboutButtonWindow():
    root = tk.Toplevel()
    root.geometry("400x400")
    label = tk.Label(root, font=100, bg="white")
    # x and y to move screen, width and height to adjust box width and height.
    label.place(width=400, height=400)
    label['text'] = "This is a Search application made \n" \
                    " by Adeel Bhatti \n" \
                    "When Searching for an item: \n" \
                    "Make sure the spelling is correct\n" \
                    "The item search is Case Sensitive"

#input validation function
def validateInput(input):
    if input.isnumeric():
        return False
    else:
        return True

url = 'https://poe.ninja/api/data/currencyoverview?league=Delirium&type=Currency&language=en'
weaponUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=UniqueWeapon&language=en'
uniqueArmourDataUrl = "https://poe.ninja/api/data/itemoverview?league=Delirium&type=UniqueArmour&language=en"
uniqueJewelsUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=UniqueJewel&language=en'
incubatorUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=Incubator&language=en'
scarabUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=Scarab&language=en'
fossilUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=Fossil&language=en'
uniqueAccessoriesUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=UniqueAccessory&language=en'
divCardsUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=DivinationCard&language=en'

fossilData = requests.get(fossilUrl)
scarabData = requests.get(scarabUrl)
incubatorData = requests.get(incubatorUrl)
uniqueJewelData = requests.get(uniqueJewelsUrl)
weaponData = requests.get(weaponUrl)
uniqueArmourData = requests.get(uniqueArmourDataUrl)
uniqueAccessoriesData = requests.get(uniqueAccessoriesUrl)
divCardsData = requests.get(divCardsUrl)
data = requests.get(url)

fossilDataJson = fossilData.json()
scarabDataJson = scarabData.json()
incubatorDataJson = incubatorData.json()
datajson = data.json()
weaponJson = weaponData.json()
uniqueArmourDataJson = uniqueArmourData.json()
uniqueJewelsDataJson = uniqueJewelData.json()
uniqueAccessoriesDataJson = uniqueAccessoriesData.json()
divCardsDataJson = divCardsData.json()



# print(datajson['lines'][0]['currencyTypeName'])
weapons = {}
currency = {}
uniqueArmourDic = {}
uniqueArmourSixLinkDic = {}
uniqueJewelsDic = {}
incubatorDic = {}
scarabPriceDic = {}
fossilPriceDic = {}
uniqueAccessoriesPriceDic = {}
divCardsPriceDic = {}

for val in divCardsDataJson['lines']:
    if val['count'] > 1:
        divCardsPriceDic[val['name']] = val['chaosValue']

for val in uniqueAccessoriesDataJson['lines']:
    if val['count'] > 1:
        uniqueAccessoriesPriceDic[val['name']] = val['chaosValue']

for val in fossilDataJson['lines']:
    if val['count'] > 1:
        fossilPriceDic[val['name']] = val['chaosValue']

for val in scarabDataJson['lines']:
    if val['count'] > 1:
        scarabPriceDic[val['name']] = val['chaosValue']

for val in incubatorDataJson['lines']:
    if val['count'] > 1:
        incubatorDic[val['name']] = val['chaosValue']

for val in uniqueJewelsDataJson['lines']:
    uniqueJewelsDic[val['name']] = val['chaosValue']

for val in uniqueArmourDataJson['lines']:
    #if  statement for isolating six links
    if val['links'] == 6:
        uniqueArmourSixLinkDic[val['name']] = val['chaosValue']

for val in uniqueArmourDataJson['lines']:
    uniqueArmourDic[val['name']] = val['chaosValue']

for val in datajson['lines']:
    currency[val['currencyTypeName']] = val['receive']['value']

for val in weaponJson['lines']:
    weapons[val['name']] = val['chaosValue']


def show_value(entry, label):
    chaosOrbs = ' Chaos Orbs'
    exaltedOrb = " Exalted Orbs"

    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(currency.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(currency.get(entry)) > exaltedOrbPrice):
            newPrice = round(currency.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(currency.get(entry))) + chaosOrbs


#function for displaying the highest valued item in the currency category..
def top_Currency_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(currency, key=currency.get)
    itemExaltPrice = round(currency.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (currency.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice, 1)) + exaltOrb
    else:

        label['text'] = max(currency.items(), key = operator.itemgetter(1))[0] + " " + str(round(currency.get(max(currency.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

#function for displaying the highest valued item in the weapon's category.
def top_Weapon_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(weapons, key=weapons.get)
    itemExaltPrice = round(weapons.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (weapons.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice)) + exaltOrb
    else:
        label['text'] = max(weapons.items(), key = operator.itemgetter(1))[0] + " " + str(round(weapons.get(max(weapons.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Armour_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(uniqueArmourDic, key=uniqueArmourDic.get)
    itemExaltPrice = round(uniqueArmourDic.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (uniqueArmourDic.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice)) + exaltOrb
    else:
        label['text'] = max(uniqueArmourDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(uniqueArmourDic.get(max(uniqueArmourDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_6LinkArmour_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(uniqueArmourSixLinkDic, key=uniqueArmourSixLinkDic.get)
    itemExaltPrice = round(uniqueArmourSixLinkDic.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (uniqueArmourSixLinkDic.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice)) + exaltOrb
    else:
        label['text'] = max(uniqueArmourSixLinkDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(uniqueArmourSixLinkDic.get(max(uniqueArmourSixLinkDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Unique_Jewel_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(uniqueJewelsDic, key=uniqueJewelsDic.get)
    itemExaltPrice = round(uniqueJewelsDic.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (uniqueJewelsDic.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice)) + exaltOrb
    else:
        label['text'] = max(uniqueJewelsDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(uniqueJewelsDic.get(max(uniqueJewelsDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Incubator_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(incubatorDic, key=incubatorDic.get)
    label['text'] = max(incubatorDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(incubatorDic.get(max(incubatorDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Scarab_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(scarabPriceDic, key=scarabPriceDic.get)
    label['text'] = max(scarabPriceDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(scarabPriceDic.get(max(scarabPriceDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Fossil_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(fossilPriceDic, key=fossilPriceDic.get)
    label['text'] = max(fossilPriceDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(fossilPriceDic.get(max(fossilPriceDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Unique_Accessories_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(uniqueAccessoriesPriceDic, key=uniqueAccessoriesPriceDic.get)
    itemExaltPrice = round(uniqueAccessoriesPriceDic.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (uniqueAccessoriesPriceDic.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice)) + exaltOrb
    else:
        label['text'] = max(uniqueAccessoriesPriceDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(uniqueAccessoriesPriceDic.get(max(uniqueAccessoriesPriceDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Div_Card_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltOrb = " Exalted Orbs"
    topCurrencyItem = max(divCardsPriceDic, key=divCardsPriceDic.get)
    itemExaltPrice = round(divCardsPriceDic.get(topCurrencyItem)) / (exaltedOrbPrice)
    if (divCardsPriceDic.get(topCurrencyItem) >= exaltedOrbPrice):
        label['text'] = str(topCurrencyItem + "\n") + str(round(itemExaltPrice, 1)) + exaltOrb
    else:
        label['text'] = max(divCardsPriceDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(divCardsPriceDic.get(max(divCardsPriceDic.items(), key = operator.itemgetter(1))[0]),)) + chaosOrbs



def show_Unique_Armour_Value(entry, label):
    chaosOrbs = " ChaosOrbs"
    exaltedOrb = " Exalted Orbs"
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(uniqueArmourDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(uniqueArmourDic.get(entry)) > exaltedOrbPrice):
            newPrice = round(uniqueArmourDic.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(uniqueArmourDic.get(entry))) + chaosOrbs



def show_Unique_Armour_Six_Lilnk_Value(entry, label):
    chaosOrbs = " ChaosOrbs"
    exaltedOrb = " Exalted Orbs"
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(uniqueArmourSixLinkDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(uniqueArmourSixLinkDic.get(entry)) > exaltedOrbPrice):
            newPrice = round(uniqueArmourSixLinkDic.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(uniqueArmourSixLinkDic.get(entry), 1)) + chaosOrbs

def show_weaponValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltedOrb = " Exalted Orbs"
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(weapons.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(weapons.get(entry)) > exaltedOrbPrice):
            newPrice = round(weapons.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(weapons.get(entry))) + chaosOrbs

def show_uniqueJewelValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltedOrb = " Exalted Orbs"
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(uniqueJewelsDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(uniqueJewelsDic.get(entry)) >= exaltedOrbPrice):
            newPrice = round(uniqueJewelsDic.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(uniqueJewelsDic.get(entry))) + chaosOrbs

def show_incubatorValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(incubatorDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:

        label['text'] = str(round(incubatorDic.get(entry))) + chaosOrbs

def show_scarabValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(scarabPriceDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        label['text'] = str(round(scarabPriceDic.get(entry))) + chaosOrbs

def show_fossilValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(fossilPriceDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        label['text'] = str(round(fossilPriceDic.get(entry))) + chaosOrbs

def show_unique_acessories_Value(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltedOrb = " Exalted Orbs"
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(uniqueAccessoriesPriceDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(uniqueAccessoriesPriceDic.get(entry)) >= exaltedOrbPrice):
            newPrice = round(uniqueAccessoriesPriceDic.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(uniqueAccessoriesPriceDic.get(entry))) + chaosOrbs

def show_Div_Cards_Value(entry, label):
    chaosOrbs = ' ChaosOrbs'
    exaltedOrb = " Exalted Orbs"
    if (entry == ""):
        label['text'] = "Please Enter a valid Item to Search for.."
    elif(str(divCardsPriceDic.get(entry)) == "None"):
        label['text'] = "Please Enter a valid Item to Search for.."
    else:
        if (round(divCardsPriceDic.get(entry)) >= exaltedOrbPrice):
            newPrice = round(divCardsPriceDic.get(entry)) / (exaltedOrbPrice)
            label['text'] = str(round(newPrice, 1)) + exaltedOrb
        else:
            label['text'] = str(round(divCardsPriceDic.get(entry))) + chaosOrbs



exaltedOrbPrice = currency.get("Exalted Orb")
print(round(exaltedOrbPrice))
root = tk.Tk()
background_image = tk.PhotoImage(file= "chest.gif")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
root.title("Currency Search Program")
#Main window title label
title = tk.Label(root,font = 200, bg="white", relief="raised")
title['text'] = "Currency Search Program"
title.place(x = 85, y = 10)

# root.configure(bg="blue")
button = tk.Button(root, text="currency search", command=main_window1)
weaponButton = tk.Button(root, text="Weapons Search (Non Six-Linked)", command=main_window2)
armourButton = tk.Button(root, text="Unique Armour Search (1-4 Links)", command=main_window3)
sixLinkedArmour = tk.Button(root, text="Six Linked Armour Search", command=main_window4)
uniqueJewels = tk.Button(root, text="uniqueJewels", command=main_window5)
incubatorButton = tk.Button(root, text = "Incubators Search", command = main_window6)
scarabButton = tk.Button(root, text = "Scarabs Search", command = main_window7)
fossilButton = tk.Button(root, text = "Fossils Search", command = main_window8)
UniqueAccessoriesButton = tk.Button(root, text = "Unique Accessories Search", command = main_window9)
divCardButton = tk.Button(root, text = "Div Cards Search", command = main_window10)
exaltRatioButton = tk.Button(root, text = "Exalt Ratio Convertor", command = exalt_Ratio_Window)
aboutButton = tk.Button(root, text="About", command=aboutButtonWindow)

button.pack()
button.place(x = 40, y = 75)
weaponButton.pack()
weaponButton.place(x = 7, y = 120)
armourButton.pack()
armourButton.place(x = 7, y = 160)
sixLinkedArmour.pack()
sixLinkedArmour.place( x = 24, y = 200)
uniqueJewels.pack()
uniqueJewels.place ( x = 40, y = 245)
incubatorButton.pack()
incubatorButton.place(x = 260, y = 75)
scarabButton.pack()
scarabButton.place(x = 267, y = 120)
fossilButton.pack()
fossilButton.place(x = 267, y = 160)
UniqueAccessoriesButton.pack()
UniqueAccessoriesButton.place( x = 230, y = 200)
divCardButton.pack()
divCardButton.place(x = 267, y = 245)
exaltRatioButton.pack()
exaltRatioButton.place( x = 140, y = 270)
tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=370)


aboutButton.pack()
aboutButton.place(x = 340, y = 370)
root.geometry("400x400+350+350")
root.mainloop()




