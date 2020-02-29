import requests
import tkinter as tk
import operator
from PIL import Image, ImageTk





def main_window2():
    root = tk.Toplevel()


    root.geometry("400x400")
    # background_image = tk.PhotoImage(file = "chest.gif")
    background_label = tk.Label(root, bg = "tomato4")
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # frame = tk.Frame(root)
    # frame.place(relwidth = 1, relheight = 1)

    entry = tk.Entry(root)
    entry.place(x = 150, y = 50, width = 100)

    # add a button
    button = tk.Button(root,text="Get Item Value", font=1, command=lambda: show_weaponValue(entry.get(), label))
    button.place(x = 1, y = 70)


    label = tk.Label(root,font = 200, bg="white")
    #x and y to move screen, width and height to adjust box width and height.
    label.place(x = 100, y = 200, width = 200, height = 200)



    tk.Button(root, text="Quit", command = root.destroy).place(x= 400, y = 750)




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



    tk.Button(root, text="Quit", command = root.destroy).place(x= 400, y = 750)




url = 'https://poe.ninja/api/data/currencyoverview?league=Metamorph&type=Currency&language=en'
weaponUrl = 'https://poe.ninja/api/data/itemoverview?league=Metamorph&type=UniqueWeapon&language=en'

weaponData = requests.get(weaponUrl)
data = requests.get(url)

datajson = data.json()
weaponJson = weaponData.json()


print(type(datajson))
# print(datajson['lines'][0]['currencyTypeName'])
weapons = {}
currency = {}

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
button.pack()
weaponButton.pack()
root.geometry("400x400+350+350")
root.mainloop()




