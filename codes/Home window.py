from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk

#importing modules of Sorting and Path Finding files
def sorting():
    pass
homeWindow = Tk()
homeWindow.title("Algorithm Visualizer")

#frames for seperation
menuFrame = Frame(homeWindow, width=200, height=600, bg="#00A6FF")
menuFrame.grid(row=0, column=0)
buttonFrame = Frame(homeWindow, width=550, height=600, bg='white')
buttonFrame.grid(row=0, column=1)

#buttons on menuFrame
menu = Button(menuFrame,width=10,text="Menu",bg="#03A6FF",border=0,fg='white',font=('verdana',16,'bold'),
              activebackground="#03A6FF",activeforeground="blue",).place(x= 20,y=30)
setting = Button(menuFrame,width=10,text="Setting",bg="#03A6FF",border=0,fg='white',font=('verdana',16,'bold'),
                 activebackground="#03A6FF",activeforeground="blue",).place(x= 20,y=80)
quit = Button(menuFrame,width=10,text="Quit",bg="#03A6FF",border=0,fg='white',font=('verdana',16,'bold'),
              activebackground="#03A6FF",activeforeground="blue",command=quit).place(x= 20,y=130)

#Menu Log ,including Sorting and Path Finding algorithm option
def image():
    global sort
    sort = ImageTk.PhotoImage(Image.open('F:\Project\Python\SY sd algo visual\imaegs\sort1.png'))
    image_label = Label(image=sort)
    image_label.place(x=250, y=70)
    image_button = Button(buttonFrame, text='Sorting', height=1, width=12, fg="white", bg="#03A6FF", border=0,
                            font=('Sans', '15', 'bold'), justify=None, activebackground="#03A6FF",
                            activeforeground="white",command=sorting)
    image_button.place(x=65, y=260)

    global path
    path = ImageTk.PhotoImage(Image.open('F:\Project\Python\SY sd algo visual\imaegs\path0.png'))
    image_label = Label(image=path)
    image_label.place(x=490, y=70)
    image_button = Button(buttonFrame, text='Path Finding', height=1, width=12, fg="white", bg="#03A6FF", border=0,
                          font=('Sans', '15', 'bold'), justify=None, activebackground="#03A6FF",
                          activeforeground="white")
    image_button.place(x=305, y=260)

if __name__ == '__main__':
    image()

homeWindow.mainloop()