from tkinter import *
import PyPDF2
from tkinter import filedialog

root = Tk()
root.title("PDF file reader")
root.geometry("500x600")
root.iconbitmap('adobereader_7073.ico')

my_text = Text(root,height=500,width=500)
my_text.pack(pady=10)

my_menu = Menu(root)
root.config(menu=my_menu)

def open_pdf():
    open_file = filedialog.askopenfilename(initialdir="C:/Desktop/ML",title="Open PDF File",filetypes=(('PDF Files','*.pdf'),('All Files','*.*')))
    if open_file:
        pdf_file = PyPDF2.PdfFileReader(open_file)
        
        page = pdf_file.getPage(0)
        page_stuff = page.extractText()
        my_text.insert(1.0,page_stuff)
        
def clear_text():
    my_text.delete(1.0,END)
        
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_separator()
file_menu.add_command(label="Clear",command=clear_text)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)


    
root.mainloop()