from tkinter import *

root = Tk()
# Creating a label widget
myLabel1 = Label(root,text="Namastey Python GUI!")
myLabel2 = Label(root,text="My name is Mainak Chaudhuri")
# Showing the widget on screen
myLabel1.grid(row=0,column=5)
myLabel2.grid(row=5,column=5)
# creating a loop to capture user interactions
root.mainloop()