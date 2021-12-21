import tkinter as tk
from datetime import datetime
import pytz
import json


class App:
    def __init__(self, root):
        root.title("Clock")
        width=350
        height=250
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.zones = json.load(open('zones.json'))
        
        self.AppLabel = tk.Label(root, text="Clock", font=("Acme", 18))
        self.AppLabel.place(x=0, y=15, width=350, height=40)
        
        self.zone = tk.StringVar()
        self.zone.set('Asia/Kolkata')
        self.zoneList = tk.OptionMenu(root, self.zone, *self.zones)
        self.zoneList.place(x=50, y=60, width=250, height=35)
        
        self.clock = tk.Label(root, font=("Acme", 45))
        self.clock.place(x=0, y=110, width=350, height=75)
        
        self.date = tk.Label(root, font=("Acme", 15))
        self.date.place(x=0, y=190, width=350, height=20)
        
    def update(self):
        self.clock.config(text=datetime.now(pytz.timezone(self.zone.get())).strftime("%I:%M:%S %p"))
        self.date.config(text=datetime.now(pytz.timezone(self.zone.get())).strftime("%A, %B %d, %Y"))
        self.clock.after(1000, self.update)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    app.update()
    root.mainloop()        