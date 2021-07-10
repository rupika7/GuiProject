from tkinter import *
root = Tk()

def myClick():
    myLable = Lable(root, text = "Button is CLicked!!")
    myLable.pack()

myButton = Button(root, text = "click" , command = myClick, fg = "red", bg = "grey")
myButton.pack()

mainloop()