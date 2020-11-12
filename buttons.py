from tkinter import *
from random import randint



root = Tk()
def clickme1():
    value = randint(1, 6)
    myLabel1 = Label(root,text="Dice")
    myLabel2 = Label(root,text=value)
    myLabel1.pack()
    myLabel2.pack()
    

    
myButton1 = Button(root,text="Click Me",command=clickme1,fg="red",bg='white',padx=50,pady=10)
myButton1.pack()

root.mainloop()