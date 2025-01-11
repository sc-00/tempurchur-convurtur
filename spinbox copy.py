import tkinter as tk
from tkinter import Menu
from tkinter import *
number = 0
fruit = ""

# create main window
root = tk.Tk()
root.title("spin box created by suling chu")
root.geometry("500x300")

def getfruit():
    global fruit
    fruit = fruitspinbox.get()
    print(fruit)

def getnumber():
    global number
    number = int(numberspinbox.get())
    print(number)

def calculate():
    global fruit, number
    if fruit == "banana":
        fruit = 3.99
        print(fruit * number)

    elif fruit == "apple":
        fruit = 2.49
        print(fruit * number)

    elif fruit == "grape":
        fruit = 2.20
        print(fruit * number)

    elif fruit == "pear":
        fruit = 2.79
        print(fruit * number)

    elif fruit == "orange":
        fruit = 2.99
        print(fruit * number)
    
fruitspinbox = tk.Spinbox(root, values = ("apple","orange","pear","banana","grape"),state = "readonly",command = getfruit)
fruitspinbox.pack(pady = 20)

numberspinbox = tk.Spinbox(root, from_ = 0,to = 10,increment = 1,state = "readonly",command = getnumber)
numberspinbox.pack(pady = 10)

button = Button(root,text = "calculate price",command = calculate)
button.pack()

root.mainloop()