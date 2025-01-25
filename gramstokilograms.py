from tkinter import *
root = Tk()
root.geometry("1000x500")

root.title("gram covurtur- suling chu")

heading = Label(root,text = "gram convurtur from gram to kilo")
heading.pack()

frame = Frame(root)
frame.pack(pady = 20)

gram = Label(frame,text = "entur number in  gram")
gram.grid(row = 0, column = 0)

cbox = Entry(frame)
cbox.grid(row = 0, column = 1)

answur = Label(frame)
answur.grid(row =2, column = 0)

def convurtur():
    g = int(cbox.get())
    kg = (g/1000)
    answur.config(text = "weight in kg "+str(kg))

convurt = Button(frame,text = "convurt",command = convurtur)
convurt.grid(row = 4, column = 0)

root.mainloop()