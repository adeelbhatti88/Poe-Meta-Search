import requests
import tkinter as tk
import operator
from PIL import Image, ImageTk

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
    entry.place(x = 50, y = 50, width = 300, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_fossilValue(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Fossil", font=1, command=lambda: top_Fossil_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Suggested Search Items:\n Exalted Orb\n Mirror of Kalandra"



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
    entry.place(x = 50, y = 50, width = 300, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_scarabValue(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Scarab", font=1, command=lambda: top_Scarab_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Suggested Search Items:\n Exalted Orb\n Mirror of Kalandra"



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)
#incubator Window
def main_window6():
    root = tk.Toplevel()

    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 50, y = 50, width = 300, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_incubatorValue(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Incubator", font=1, command=lambda: top_Incubator_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Suggested Search Items:\n Exalted Orb\n Mirror of Kalandra"



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)
#uniqueJewels window
def main_window5():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 50, y = 50, width = 300, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_uniqueJewelValue(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Unique Jewel", font=1, command=lambda: top_Unique_Jewel_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


#unique armour six link armour window
def main_window4():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 50, y = 50, width = 300, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Unique_Armour_Six_Lilnk_Value(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top 6-Link Armour", font=1, command=lambda: top_6LinkArmour_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    # label2 = tk.Label(root, font = 200, bg="white")
    # label2.place(x=45, y = 25)
    # label2['text'] = "Results will be value of 1-4 linked armours only"



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)

#unique armour window
def main_window3():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 50, y = 50, width = 300, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Unique_Armour_Value(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Armour", font=1, command=lambda: top_Armour_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)






    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


#weapon window
def main_window2():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 50, y = 50, width = 300, height = 50)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_weaponValue(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Weapon", font=1, command=lambda: top_Weapon_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)



#currency window
def main_window1():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root, font=("Calibri 24"))
    entry.place(x = 50, y = 50, width = 300, height = 50)
    #user input testing
    reg = root.register(validateInput)
    entry.config(validate="key",validatecommand=(reg, '%P'))

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_value(entry.get(), label))
    button.place(x = 1, y = 100, height = 50)

    button2 = tk.Button(root, text="Top Currency", font=1, command=lambda: top_Currency_Item(entry.get(), label))
    button2.place(x=150, y=100, height = 50)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Suggested Search Items:\n Exalted Orb\n Mirror of Kalandra"



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


def aboutButtonWindow():
    root = tk.Toplevel()
    root.geometry("400x400")
    message = tk.Message(root, text="This app is made by adeel Bhatti, This app lets you serach various currency items, unique armours, and unique weapons from the game Path of Exile.")
    message.pack()

    tk.Button(root, text="Quit", command=root.destroy).place(x=175, y=375)

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

fossilData = requests.get(fossilUrl)
scarabData = requests.get(scarabUrl)
incubatorData = requests.get(incubatorUrl)
uniqueJewelData = requests.get(uniqueJewelsUrl)
weaponData = requests.get(weaponUrl)
uniqueArmourData = requests.get(uniqueArmourDataUrl)
data = requests.get(url)

fossilDataJson = fossilData.json()
scarabDataJson = scarabData.json()
incubatorDataJson = incubatorData.json()
datajson = data.json()
weaponJson = weaponData.json()
uniqueArmourDataJson = uniqueArmourData.json()
uniqueJewelsDataJson = uniqueJewelData.json()


print(type(datajson))
# print(datajson['lines'][0]['currencyTypeName'])
weapons = {}
currency = {}
uniqueArmourDic = {}
uniqueArmourSixLinkDic = {}
uniqueJewelsDic = {}
incubatorDic = {}
scarabPriceDic = {}
fossilPriceDic = {}

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

print(uniqueJewelsDic)
def show_value(entry, label):
    chaosOrbs = ' ChaosOrbs'
    print("inside show value function!!", entry)
    print(currency.get(entry))
    label['text'] = str(currency.get(entry)) + chaosOrbs

#function for displaying the highest valued item in the currency category..
def top_Currency_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(currency, key=currency.get)
    label['text'] = max(currency.items(), key = operator.itemgetter(1))[0] + " " + str(round(currency.get(max(currency.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

#function for displaying the highest valued item in the weapon's category.
def top_Weapon_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(weapons, key=weapons.get)
    label['text'] = max(weapons.items(), key = operator.itemgetter(1))[0] + " " + str(round(weapons.get(max(weapons.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Armour_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(uniqueArmourDic, key=uniqueArmourDic.get)
    label['text'] = max(uniqueArmourDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(uniqueArmourDic.get(max(uniqueArmourDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_6LinkArmour_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(uniqueArmourSixLinkDic, key=uniqueArmourSixLinkDic.get)
    label['text'] = max(uniqueArmourSixLinkDic.items(), key = operator.itemgetter(1))[0] + " " + str(round(uniqueArmourSixLinkDic.get(max(uniqueArmourSixLinkDic.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs

def top_Unique_Jewel_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(uniqueJewelsDic, key=uniqueJewelsDic.get)
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



def show_Unique_Armour_Value(entry, label):
    chaosOrbs = " ChaosOrbs"
    label['text'] = str(uniqueArmourDic.get(entry)) + chaosOrbs

def show_Unique_Armour_Six_Lilnk_Value(entry, label):
    chaosOrbs = " ChaosOrbs"
    label['text'] = str(uniqueArmourSixLinkDic.get(entry)) + chaosOrbs

def show_weaponValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(weapons.get(entry)) + chaosOrbs

def show_uniqueJewelValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(uniqueJewelsDic.get(entry)) + chaosOrbs

def show_incubatorValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(incubatorDic.get(entry)) + chaosOrbs

def show_scarabValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(scarabPriceDic.get(entry)) + chaosOrbs

def show_fossilValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(fossilPriceDic.get(entry)) + chaosOrbs


root = tk.Tk()
background_image = tk.PhotoImage(file= "chest.gif")
background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
root.title("Currency Search Program")

# root.configure(bg="blue")
button = tk.Button(root, text="currency search", command=main_window1)
weaponButton = tk.Button(root, text="Weapons Search", command=main_window2)
armourButton = tk.Button(root, text="Unique Armour Search (1-4 Links)", command=main_window3)
sixLinkedArmour = tk.Button(root, text="Six Linked Armour Search", command=main_window4)
uniqueJewels = tk.Button(root, text="uniqueJewels", command=main_window5)
incubatorButton = tk.Button(root, text = "Incubators", command = main_window6)
scarabButton = tk.Button(root, text = "Scarabs", command = main_window7)
fossilButton = tk.Button(root, text = "Fossils", command = main_window8)
aboutButton = tk.Button(root, text="About", command=aboutButtonWindow)
button.pack()
weaponButton.pack()
armourButton.pack()
sixLinkedArmour.pack()
uniqueJewels.pack()
incubatorButton.pack()
scarabButton.pack()
fossilButton.pack()
aboutButton.pack()
root.geometry("400x400+350+350")
root.mainloop()




