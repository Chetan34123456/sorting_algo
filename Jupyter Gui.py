import os
from tkinter import *
from tkinter import ttk

jupyter=Tk()

def runNb():
    try:
        
        os.system("jupyter notebook")
    except Exception:
        message.showinfo(END,"Error occured")
a=Button(jupyter,text="Start Notebook",width=15,bg="Sky blue",font=("Verdana",16),command=runNb)
a.pack()
jupyter.mainloop()