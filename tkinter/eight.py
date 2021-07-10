from tkinter import *
root = Tk()

e1 = Entry(root, width = 20, fg = "blue", bg = "white", borderwidth = 5)
e1.pack()

def myClick():
    textoutput = "Hello " + e1.get()
    myLable = Label(root, text = textoutput)
    myLable.pack()

    myButton = Button(root, text = textoutput)
    myButton.pack()

myButton = Button(root, text = "Click Me!", command = myClick)
myButton.pack()
mainloop()