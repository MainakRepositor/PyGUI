import tkinter as tk
import cryptocode


class App:
    def __init__(self, root):
        root.title("Text Encryption")
        width=350
        height=280
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        self.AppLabel = tk.Label(root, text="Text Encryption", font=("Acme", 24))
        self.AppLabel.place(x=0, y=15, width=350, height=30)
        
        self.TextLabel = tk.Label(root, text="Text:", font=("Acme", 16))
        self.TextLabel.place(x=10, y=60, width=100, height=30)
        
        self.TextEntry = tk.Entry(root, font=("Acme", 16))
        self.TextEntry.place(x=110, y=60, width=230, height=30)
        
        self.KeyLabel = tk.Label(root, text="Key:", font=("Acme", 16))
        self.KeyLabel.place(x=10, y=100, width=100, height=30)
        
        self.KeyEntry = tk.Entry(root, font=("Acme", 16))
        self.KeyEntry.place(x=110, y=100, width=230, height=30)
        
        self.EncryptButton = tk.Button(root, text="Encrypt", font=("Acme", 16), command=self.Encrypt)
        self.EncryptButton.place(x=10, y=140, width=330, height=30)
        
        self.DecryptButton = tk.Button(root, text="Decrypt", font=("Acme", 16), command=self.Decrypt)
        self.DecryptButton.place(x=10, y=180, width=330, height=30)
        
        self.ResultLabel = tk.Label(root, text="Result:", font=("Acme", 16))
        self.ResultLabel.place(x=10, y=220, width=100, height=30)
        self.ResultEntry = tk.Entry(root, font=("Acme", 16))
        self.ResultEntry.place(x=110, y=220, width=230, height=30)
        self.ResultEntry.config(state="disabled")
        
    def Encrypt(self):
        text = self.TextEntry.get()
        key = self.KeyEntry.get()
        result = cryptocode.encrypt(text, key)
        self.ResultEntry.config(state="normal")
        self.ResultEntry.delete(0, tk.END)
        self.ResultEntry.insert(0, result)
        # self.ResultEntry.config(state="disabled")
        
    def Decrypt(self):
        text = self.TextEntry.get()
        key = self.KeyEntry.get()
        result = cryptocode.decrypt(text, key)
        self.ResultEntry.config(state="normal")
        self.ResultEntry.delete(0, tk.END)
        self.ResultEntry.insert(0, result)
        # self.ResultEntry.config(state="disabled")
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()