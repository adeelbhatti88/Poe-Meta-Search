import requests
import tkinter as tk
import operator
from PIL import Image, ImageTk

#unique armour six link armour window
def main_window4():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root)
    entry.place(x = 50, y = 50, width = 300)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Unique_Armour_Six_Lilnk_Value(entry.get(), label))
    button.place(x = 1, y = 70)

    button2 = tk.Button(root, text="Top Weapon", font=1, command=lambda: top_Weapon_Item(entry.get(), label))
    button2.place(x=150, y=70)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 100, y = 200, width = 200, height = 200)
    label2 = tk.Label(root, font = 200, bg="white")
    label2.place(x=45, y = 25)
    label2['text'] = "Results will be value of 1-4 linked armours only"



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

    entry = tk.Entry(root)
    entry.place(x = 50, y = 50, width = 300)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_Unique_Armour_Value(entry.get(), label))
    button.place(x = 1, y = 70)

    button2 = tk.Button(root, text="Top Weapon", font=1, command=lambda: top_Weapon_Item(entry.get(), label))
    button2.place(x=150, y=70)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 100, y = 200, width = 200, height = 200)
    label2 = tk.Label(root, font = 200, bg="white")
    label2.place(x=45, y = 25)
    label2['text'] = "Results will be value of 1-4 linked armours only"



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

    entry = tk.Entry(root)
    entry.place(x = 50, y = 50, width = 300)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_weaponValue(entry.get(), label))
    button.place(x = 1, y = 70)

    button2 = tk.Button(root, text="Top Weapon", font=1, command=lambda: top_Weapon_Item(entry.get(), label))
    button2.place(x=150, y=70)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 100, y = 200, width = 200, height = 200)



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

    entry = tk.Entry(root)
    entry.place(x = 50, y = 50, width = 300)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_value(entry.get(), label))
    button.place(x = 1, y = 70)

    button2 = tk.Button(root, text="Top Currency", font=1, command=lambda: top_Currency_Item(entry.get(), label))
    button2.place(x=150, y=70)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 0, y = 200, width = 400, height = 200)
    label['text'] = "Suggested Search Items: Exalted Orb, Mirror of Kalandra"



    tk.Button(root, text="Quit", command = root.destroy).place(x=175, y=375)


def aboutButtonWindow():
    root = tk.Toplevel()
    root.geometry("400x400")
    message = tk.Message(root, text="This app is made by adeel Bhatti, This app lets you serach various currency items, unique armours, and unique weapons from the game Path of Exile.")
    message.pack()

    tk.Button(root, text="Quit", command=root.destroy).place(x=175, y=375)





url = 'https://poe.ninja/api/data/currencyoverview?league=Delirium&type=Currency&language=en'
weaponUrl = 'https://poe.ninja/api/data/itemoverview?league=Delirium&type=UniqueWeapon&language=en'
uniqueArmourDataUrl = "https://poe.ninja/api/data/itemoverview?league=Delirium&type=UniqueArmour&language=en"

weaponData = requests.get(weaponUrl)
uniqueArmourData = requests.get(uniqueArmourDataUrl)
data = requests.get(url)

datajson = data.json()
weaponJson = weaponData.json()
uniqueArmourDataJson = uniqueArmourData.json()


print(type(datajson))
# print(datajson['lines'][0]['currencyTypeName'])
weapons = {}
currency = {}
uniqueArmourDic = {}
uniqueArmourSixLinkDic = {}

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

print(currency)
def show_value(entry, label):
    chaosOrbs = ' ChaosOrbs'
    print("inside show value function!!", entry)
    print(currency.get(entry))
    label['text'] = str(currency.get(entry)) + chaosOrbs

#function for displaying the highest valued item in the currency category..
def top_Currency_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(currency, key=currency.get)
    label['text'] = max(currency.items(), key = operator.itemgetter(1))[0] + " " + str(round(currency.get(max(currency.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs + "\n we in this" + "\n and another one"

#function for displaying the highest valued item in the weapon's category.
def top_Weapon_Item(entry, label):
    chaosOrbs = ' ChaosOrbs'
    topCurrencyItem = max(weapons, key=weapons.get)
    label['text'] = max(weapons.items(), key = operator.itemgetter(1))[0] + " " + str(round(weapons.get(max(weapons.items(), key = operator.itemgetter(1))[0]))) + chaosOrbs + "\n we in this" + "\n and another one"


def show_Unique_Armour_Value(entry, label):
    chaosOrbs = " ChaosOrbs"
    label['text'] = str(uniqueArmourDic.get(entry)) + chaosOrbs

def show_Unique_Armour_Six_Lilnk_Value(entry, label):
    chaosOrbs = " ChaosOrbs"
    label['text'] = str(uniqueArmourSixLinkDic.get(entry)) + chaosOrbs

def show_weaponValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(weapons.get(entry)) + chaosOrbs


root = tk.Tk()
background_image = tk.PhotoImage(file= "chest.gif")

background_label = tk.Label(root, image=background_image)
background_label.place(x=0,y=0,relwidth=1,relheight=1)

# root.configure(bg="blue")
button = tk.Button(root, text="currency search", command=main_window1)
weaponButton = tk.Button(root, text="Weapons Search", command=main_window2)
armourButton = tk.Button(root, text="Unique Armour Search", command=main_window3)
sixLinkedArmour = tk.Button(root, text="Six Linked Armour Search", command=main_window4)
aboutButton = tk.Button(root, text="About", command=aboutButtonWindow)
button.pack()
weaponButton.pack()
armourButton.pack()
sixLinkedArmour.pack()
aboutButton.pack()
root.geometry("400x400+350+350")
root.mainloop()




