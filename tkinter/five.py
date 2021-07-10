from tkinter import *
root = Tk()
#creating a label widget
myLable1 = Label(root, text = "Tkinter Program Begining")
myLable2 = Label(root, text = "gkjdhfkjdsh    ")
myLable3 = Label(root, text = "I Am Rupika Rasaili")

#shoving ir onto the screen based on x-axis and y-axis
#that does not move having a constant position
myLable1.grid( row = 0, column = 0)
myLable2.grid( row = 1, column = 5)
myLable3.grid( row = 1, column = 1)
mainloop()
