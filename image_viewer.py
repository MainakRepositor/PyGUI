from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title('My Image Viewer')
root.iconbitmap('Camera_Next_30014 (1).ico')

img1 = ImageTk.PhotoImage(Image.open('images/al1.png'))
img2 = ImageTk.PhotoImage(Image.open('images/Alex.jpg'))
img3 = ImageTk.PhotoImage(Image.open('images/code.jpg'))
img4 = ImageTk.PhotoImage(Image.open('images/for.jpg'))
img5 = ImageTk.PhotoImage(Image.open('images/king.jpg'))
img6 = ImageTk.PhotoImage(Image.open('images/Leo.jpg'))
img7 = ImageTk.PhotoImage(Image.open('images/lion.png'))
img8 = ImageTk.PhotoImage(Image.open('images/me.png'))
img9 = ImageTk.PhotoImage(Image.open('images/Pengu.png'))
img10 = ImageTk.PhotoImage(Image.open('images/shiva.jpg'))
img11 = ImageTk.PhotoImage(Image.open('images/pic.jpg'))
img12 = ImageTk.PhotoImage(Image.open('images/space.png'))

img_list = [img1,img2,img3,img4,img5,img6,img7,img8,img9,img10,img11,img12]


mylabel = Label(image=img1)
mylabel.grid(row=0,column=0,columnspan=3)

def front(img_num):
    global mylabel
    global button_next
    global button_prev
    
    mylabel.grid_forget()
    mylabel = Label(image=img_list[img_num-1])
    button_next = Button(root,text="next >>",command=lambda:front(img_num+1))
    button_prev = Button(root,text="<< previous",command=lambda:previous(img_num-1))
    
    if img_num == len(img_list):
        button_next = Button(root,text="next >>",state=DISABLED)
        
        
    
    mylabel.grid(row=0,column=0,columnspan=3)
    button_prev.grid(row=1,column=0)
    button_next.grid(row=1,column=2)
    
    
def previous(img_num):
    global mylabel
    global button_next
    global button_prev
    mylabel.grid_forget()
    mylabel = Label(image=img_list[img_num-1])
    button_next = Button(root,text="next >>",command=lambda:front(img_num+1))
    button_prev = Button(root,text="<< previous",command=lambda:previous(img_num-1))
    
    #if img_num == 1:
        #button_prev = Button(root,text="<< previous",state=DISABLED)
        
    
    mylabel.grid(row=0,column=0,columnspan=3)
    button_prev.grid(row=1,column=0)
    button_next.grid(row=1,column=2)
    
    

button_prev = Button(root,text="<< previous",command=lambda:previous())
button_end = Button(root,text="Exit System",command=root.quit)
button_next = Button(root,text="next >>",command=lambda:front(2))

button_prev.grid(row=1,column=0)
button_end.grid(row=1,column=1)
button_next.grid(row=1,column=2)

root.mainloop()


