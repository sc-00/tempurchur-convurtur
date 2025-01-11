from tkinter import *
root = Tk()
root.geometry("1000x500")

root.title("tempurture covurtur- suling chu")

heading = Label(root,text = "tempurchur convurtur from °C to °F")
heading.pack()

frame = Frame(root)
frame.pack(pady = 20)

temp = Label(frame,text = "entur tempurchur in  °C")
temp.grid(row = 0, column = 0)

cbox = Entry(frame)
cbox.grid(row = 0, column = 1)

answur = Label(frame)
answur.grid(row =2, column = 0)

def convurtur():
    C = int(cbox.get())
    F = ((C)*9/5)+32
    answur.config(text = "tempurchur in °F "+str(F))

convurt = Button(frame,text = "convurt",command = convurtur)
convurt.grid(row = 4, column = 0)

root.mainloop()