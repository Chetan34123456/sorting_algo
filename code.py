
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

code=Tk()
code.geometry("935x600")
code.resizable(width=False, height=False)
def messagebox(self, code, text):
    '''
    gives message window
    :parm code:  word for message
    :parm text:
    :return : message box
    '''
    if code == None:
        code = "Error"
    return messagebox.showinfo(code, text)

def cLang():
    pass
def cplusLang():
    pass

def python():
    pass

def java():
    pass



codeFrame=Frame(code,width=750,height=600,bg="#2D5FFF").place(x=150,y=0)
codeScroll=Scrollbar(codeFrame)
codeScroll.pack(side=RIGHT,fill=Y)
codeText=Text(codeFrame,width=92,height=27,yscrollcommand=codeScroll.set)
codeText.place(x=155,y=0)
codeScroll.config(command=codeText.yview)

textScroll=Scrollbar(codeFrame)
textScroll.pack(side=RIGHT,fill=Y)
textListBox=Listbox(codeFrame,width=122,height=9,yscrollcommand=textScroll.set)
textListBox.place(x=155,y=445)
textScroll.config(command=textListBox.yview)

buttonFrame=Frame(code,width=150,height=600,bg="grey").place(x=0,y=0)
cButton=Button(buttonFrame,text="C",width=10,command= cLang).place(x=30,y=30)
cPlusButton=Button(buttonFrame,text="C++",width=10).place(x=30,y=70)
pythonButton=Button(buttonFrame,text="Python",width=10).place(x=30,y=110)
javaButton=Button(buttonFrame,text="Java",width=10).place(x=30,y=150)

code.mainloop()

