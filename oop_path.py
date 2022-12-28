print("Hello")
# imports
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from algo import *

pathFinding = Tk()
pathFinding.title("Algo Visual - Path Finding")
pathFinding.config(bg="#2D5FFF")
pathFinding.geometry("1600x1600")

# variables
pathSelectAlgo = StringVar()
block_list = []

# frame definations
buttonFrame = Frame(pathFinding, width=1000, height=100, bg='white')
buttonFrame.grid(row=0, column=0, padx=10, pady=10)
workSpace = Canvas(pathFinding, width=1000, height=700, bg="grey")
workSpace.grid(row=1, column=0, padx=10, pady=10)
algoInfoFrame = Frame(pathFinding, width=500, height=100)
algoInfoFrame.place(x=1020, y=10)
algoStepFrame = Frame(pathFinding, width=500, height=100)
algoStepFrame.place(x=1020, y=280)
algoLinkFrame = Frame(pathFinding, width=500, height=100)
algoLinkFrame.place(x=1020, y=550)

# definations


def message(code, text):
    return messagebox.showinfo(code, text)


# building Buttons


class buildingBlocks:

    def __init__(self):

        self.block_index = 0
        self.start_points = []
        self.end_points = []

        for x in range(20):
            for y in range(14):
                self.block_index = self.block_index + 1
                workSpace.create_rectangle(x*50, y*50, x*50+50, y*50+50, fill='white')
                workSpace.create_text(x*50+25, y*50+25, text=f"{str(x+1)}, {str(y+1)}")
        self.bind()

    def bind(self):

        workSpace.bind("<Button-1>", self.identify_block)

    def identify_block(self,event):
        print(event.x, event.y)
        self.x_cord, self.y_cord=event.x//50, event.y//50

        workSpace.create_rectangle(self.x_cord*50, self.y_cord*50, self.x_cord*50 + 50,
                                   self.y_cord * 50 + 50, fill='purple')
        workSpace.create_text(self.x_cord * 50 + 25, self.y_cord * 50 + 25, text=f"{str(self.x_cord + 1)}, {str(self.y_cord + 1)}")

    def generate_obs(self):

        self.random_obs_x = []
        self.random_obs_y = []

        for i in range(100):
            self.random_obs_x.append(random.randrange(0,20))
            self.random_obs_y.append(random.randrange(0,14))

        #print(f"{self.random_obs_x}, {self.random_obs_y}")

        for obs in range(100):
            workSpace.create_rectangle(self.random_obs_x[obs] * 50, self.random_obs_y[obs] * 50, self.random_obs_x[obs] * 50 + 50,
                                       self.random_obs_y[obs] * 50 + 50, fill='grey')
            workSpace.create_text(self.random_obs_x[obs] * 50 + 25, self.random_obs_y[obs] * 50 + 25, text=f"{str(self.random_obs_x[obs] + 1)}, {str(self.random_obs_y[obs] + 1)}")
        print(f"Obs : x = {self.random_obs_x}")
        print(f"Obs: y = {self.random_obs_y}")

    def starting_pt(self):
        self.start_points_temp=[self.x_cord, self.y_cord]
        self.start_points.append(self.start_points_temp)

        for temp in self.start_points:
                workSpace.create_rectangle(temp[0] * 50, temp[1] * 50, temp[0] * 50 + 50,
                                           temp[1] * 50 + 50, fill='white')
                workSpace.create_text(self.x_cord * 50 + 25, self.y_cord * 50 + 25,
                                      text=f"{str(self.x_cord + 1)}, {str(self.y_cord + 1)}")

        workSpace.create_rectangle(self.x_cord * 50, self.y_cord * 50, self.x_cord * 50 + 50,
                                self.y_cord * 50 + 50, fill='green')
        workSpace.create_text(self.x_cord * 50 + 25, self.y_cord * 50 + 25, text=f"{str(self.x_cord + 1)}, {str(self.y_cord + 1)}")
        print(f"Start : {self.x_cord},{self.y_cord}")

    def destination(self):

        self.end_points_temp = [self.x_cord, self.y_cord]
        self.end_points.append(self.end_points_temp)

        for temp in self.end_points:
            workSpace.create_rectangle(temp[0] * 50, temp[1] * 50, temp[0] * 50 + 50,
                                       temp[1] * 50 + 50, fill='white')
            workSpace.create_text(temp[0] * 50 + 25, temp[1]* 50 + 25, text=f"{str(temp[0] + 1)}, {str(temp[1] + 1)}")

        workSpace.create_rectangle(self.x_cord * 50, self.y_cord * 50, self.x_cord * 50 + 50,
                                   self.y_cord * 50 + 50, fill='red')
        workSpace.create_text(self.x_cord * 50 + 25, self.y_cord * 50 + 25, text=f"{str(self.x_cord + 1)}, {str(self.y_cord + 1)}")
        print(f"Destination: {self.x_cord},{self.y_cord}")


build = buildingBlocks()

# buttons and labels
pathAlgoLabel = Label(buttonFrame, text='Algorithm',width=15)
pathAlgoLabel.grid(row=0,column=0,pady=10)
pathalgMenu = ttk.Combobox(buttonFrame, textvariable=pathSelectAlgo, values=["BFS", "DFS","A star"], width=17)
pathalgMenu.grid(row=0, column=1, padx=5, pady=10)
pathalgMenu.current(0)

selectStartPt = Button(buttonFrame, width= 15, text = "Select Start Point", border = 1,command=build.starting_pt)
selectStartPt.grid(row = 1, column = 0, padx = 10, pady=10)

generateObs = Button(buttonFrame, width = 15, text = 'Generate Obstracles', border = 1, command = build.generate_obs)
generateObs.grid(row = 0, column = 2, padx = 10,pady=10)

selectObs = Button(buttonFrame, width =15, text = 'Select Obstracles', border = 1, command = '#')
selectObs.grid(row = 0, column = 3, padx =10,pady=10)

selectEndPt = Button(buttonFrame, width = 15, text = 'Destination Point', border = 1, command=build.destination)
selectEndPt.grid(row = 1,column = 1, padx =10, pady =10)

run = Button(buttonFrame, width =15, text = 'Run', border = 1)
run.grid(row = 1, column =2, padx =10, pady =10)

# listBOxes
infoScrollbar = Scrollbar(algoInfoFrame)
infoScrollbar.pack(side=RIGHT,fill = Y)
infoListBox = Listbox(algoInfoFrame, width=60, height=15, font=("Verdana", 10),yscrollcommand= infoScrollbar.set)
infoListBox.pack(side = LEFT,fill =BOTH)
infoScrollbar.config(command=infoListBox.yview)

stepScrollbar = Scrollbar(algoStepFrame)
stepScrollbar.pack(side=RIGHT,fill = Y)
stepListBox = Listbox(algoStepFrame, width=60, height=15, font=("Verdana", 10),yscrollcommand= stepScrollbar.set)
stepListBox.pack(side = LEFT,fill =BOTH)
stepScrollbar.config(command=stepListBox.yview)

linkScrollbar = Scrollbar(algoLinkFrame)
linkScrollbar.pack(side=RIGHT,fill = Y)
linkListBox = Listbox(algoLinkFrame, width=60, height=16, font=("Verdana", 10), yscrollcommand= linkScrollbar.set)
linkListBox.pack(side=LEFT,fill=BOTH)
linkScrollbar.config(command=linkListBox.yview)

pathFinding.mainloop()