from tkinter import *

root = Tk()

e = Entry(root,width=50,fg='blue',borderwidth=7)
e.pack()
e.insert(1, "Enter your name : ")

def myclick():
    l = int(len(e.get()))
    mylabel = Label(root,text="Hello  "+e.get()+" !")
    mylabel1 = Label(root,text="Length of your name : ")
    mylabel2 = Label(root,text=l)
    mylabel.pack()
    mylabel1.pack()  
    mylabel2.pack()
    
mybutton = Button(root,text="Insert",command=myclick)
mybutton.pack()

root.mainloop()