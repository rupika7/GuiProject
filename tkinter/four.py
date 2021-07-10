from tkinter import *
root = Tk()

mybutton = Button(root, text = "Click Me")
mybutton.pack()

mybutton1 = Button(root, text = "Click", state = DISABLED)
mybutton1.pack()

mybutton2 = Button(root, text = "Click", padx = 50)
mybutton2.pack()
mybutton3 = Button(root, text = "Click",padx = 50, pady = 50)
mybutton3.pack()
mainloop()
