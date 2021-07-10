from tkinter import *
root = Tk()

def myCLick():
    myLable = Label(root, text = "Buttton is clicked!!")
    myLable.pack()

myButton = Button(root, text = "Click Me!", command = myCLick)
myButton.pack()

mainloop()