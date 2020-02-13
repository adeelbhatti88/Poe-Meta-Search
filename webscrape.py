
import requests
import tkinter as tk


def open_window():
    root = tk.Tk()
    root.configure(bg="blue")
    button = tk.Button(root, text="currency search", command=main_window1)
    weaponButton = tk.Button(root, text="Weapons Search", command=main_window2)
    button.pack()
    weaponButton.pack()
    root.geometry("400x400+150+150")
    root.mainloop()

def main_window2():
    root = tk.Tk()
    HEIGHT = 700
    WIDTH = 800
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()  # the .pack displays it on the screen

    frame = tk.Frame(root, bg='blue', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    # add a button
    button = tk.Button(frame, text="Get Item Value", font=40, command=lambda: show_weaponValue(entry.get(), label))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = tk.Frame(root, bg='blue', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)



    tk.Button(root, text="Quit", command = root.destroy).pack()

def main_window1():
    root = tk.Tk()
    HEIGHT = 700
    WIDTH = 800
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()  # the .pack displays it on the screen

    frame = tk.Frame(root, bg='blue', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    # add a button
    button = tk.Button(frame, text="Get Item Value", font=40, command=lambda: show_value(entry.get(), label))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = tk.Frame(root, bg='blue', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)



    tk.Button(root, text="Quit", command = root.destroy).pack()



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



def show_weaponValue(entry, label):
    chaosOrbs = ' ChaosOrbs'
    label['text'] = str(weapons.get(entry)) + chaosOrbs


open_window()


