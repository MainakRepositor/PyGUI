from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title("Icons and Images")
root.iconbitmap('among_us_player_blue_icon_156941.ico')

mylabel1 = Label(root,text="Be Lionic",font=20)
mylabel1.pack()
img = ImageTk.PhotoImage(Image.open('Leo.jpg'))
mylabel = Label(image=img)
mylabel.pack()


button_quit = Button(root,text='Exit',padx=5,pady=5,borderwidth=5,command=root.quit)
button_quit.pack()



root.mainloop()