
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as message
import random
from algo import *

# forming the window
sort = Tk()
sort.title("Algo Visual - Sorting")
sort.config(bg="#2D5FFF")
sort.geometry("1550x1600")

# variables
selectAlg = StringVar()
data = []

# definations
class drawAlgo:
    '''
    responsible for all actions of GUI
    '''
    def __init__(self):
        self.title = "Key points:-"
        self.bubbleSort = [self.title, " ", "Algorithm = Bubble sort Algorithm\n", "Time Complexcity :-\n", "Best Case :-n",
                     "Average Case :- n^2", "Worst Case :- n^2", "Space Complexity :- 1", "Based on :- Divide and Conquer\n"]
        self.mergeSort = [self.title, " ", "Algorithm = Merge sort Algorithm\n", "Time Complexcity :-\n", "Best Case :-n*log(n)",
                     "Average Case :- n*log(n)", "Worst Case :- n*log(n)","Space Complexity :- n", "Based on :- Divide and Conquer\n"]
        self.selectionSort = [self.title, " ", "Algorithm = Selection sort Algorithm\n", "Time Complexcity :-\n", "Best Case :- n^2",
                     "Average Case :- n^2", "Worst Case :- n^2","Space Complexity :- 1", "Based on :- \n"]
        self.insertionSort = [self.title, " ", "Algorithm = Insertion sort Algorithm\n", "Time Complexcity :-\n", "Best Case :- n ",
                     "Average Case :- n^2", "Worst Case :- n^2","Space Complexity :- 1", "Based on :- \n"]
        self.linearSearch = [self.title, " ", "Algorithm =Linear Search Algorithm\n", "Time Complexcity :-\n",
                              "Best Case :- n ","Average Case :- n^2", "Worst Case :- n^2", "Space Complexity :- 1", "Based on :- \n"]
        self.steps = ""
        self.links = ""

    def messagebox(self, code, text):
        '''
        gives message window
        :parm code: code word for message
        :parm text: message
        :return : message box
        '''
        if code == None:
            code = "Error"
        return message.showinfo(code, text)

    def draw(self, data, color):
        '''
        responsible to draw bars for Sorting Algorithm
        :parm data: array on which different algorithm will perform
        :parm color: determines colour of all during visualization process
        :return : None
        '''
        baseCanvas.delete("all")
        self.canvasHt = 400
        self.canvasWt = 1400
        self.bar_width = self.canvasWt / (len(self.data) + 1)
        self.shift = 40  # moves the bars in x direction (less offset = more towards left)
        self.spacing = 5  # space between the bars
        self.normalizedData = [i / max(data) for i in
                               data]  # normalized data scales the orignal data to fit properly in graph

        for i, height in enumerate(self.normalizedData):
            x0 = i * self.bar_width + self.shift + self.spacing
            y0 = self.canvasHt - height * 300
            x1 = (i + 1) * self.bar_width + self.shift
            y1 = self.canvasHt  # to start the bar from end of canvas

            baseCanvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
            #print(f"{color[i]}=color , length ={len(color)}")
            baseCanvas.create_text(x0 + 2, y0, anchor=SW, text=str(self.data[i]),font=("vergana",16))
            baseCanvas.create_text(x1-self.bar_width/2,y1+15, text = i,font = ('vergana',16))
            #  anchor used to shift the text in centre of bars
        sort.update_idletasks()

    def drawMerge(self,data,color):
        '''
        makes square shape for merge sort
        :parm data: array on which different algorithm will perform
        :parm color: determines colour of all during visualization process
        :return : None
        in progress
        '''
        baseCanvas.delete("all")
        x0, y0, x1, y1 = 0, 0, 0, 0
        width = 50
        spacing = 10
        shift = 50
        #showing whole array
        for _ in range(len(self.data)):
                x0 = width * (_) + spacing + shift + 300
                y0 = width
                x1 = x0 + width +300
                y1 = width * 2
                baseCanvas.create_rectangle(x0, y0, x1, y1, fill=color[0])
                a = x0, y0, x1, y1
                print(a)

        for j in range(len(self.data) + 1):
            print(j)
            print(x0, y0, x1, y1)
            for i in range(len(self.data)):
                x0 = width * (i) + spacing + shift
                y0 = width + j * 100 +50
                x1 = x0 + width
                y1 = width * 2 + j * 100+50
                baseCanvas.create_rectangle(x0, y0, x1, y1, fill=color[j])
                a = x0, y0, x1, y1
                print(a)

    def showDataSet(self):
        '''
        responsible to selecting array parameter
        :return: None
        '''
        global data
        print("Algo selected :" + selectAlg.get())
        self.minVal, self.maxVal, self.sizeVal, self.element = 0, 0, 0, None
        try:
            self.minVal = int(minEntry.get())
            self.maxVal = int(maxEntry.get())
            self.sizeVal = int(sizeEntry.get())
            self.speedLim = int(speedLimit.get())
        except Exception:
            self.messagebox("Error","Please enter integer value..")
        self.data = []
        for i in range(self.sizeVal):
            self.data.append(random.randrange(self.minVal, self.maxVal + 1))
        self.draw(self.data, ["sky blue" for i in range(len(self.data))])

    def runAll(self):
        '''
        Created to print all information related to algorithm
        :return: None
        '''
        self.linklist(self.steps)
        self.shortlist()
        self.steplist(self.links)

    def steplist(self, steps):
        '''
        prints all steps performed by algorithm
        :parm steps: receive all steps and print in respected listbox
        :return: None
        '''
        stepListBox.insert(END, steps)
        stepListBox.see('end')
    def linklist(self, links):
        '''
        prints all links and study material related to algorithm
        :parm links: receive all links and print in respected listbox
        :return : None
        '''
        linkListBox.insert(END,"Important Links")
        linkListBox.insert(END,"             ")
        linkListBox.insert(END, links)
        linkListBox.see('end')

    def shortlist(self):
        '''
        prints all performance related parameters in respective linkbox.
        it includes :- algorithm name,time complexcity,space complexcity
                       ,based on.
        :return: None
        '''
        if selectAlg.get()=="Bubble Sort":
            for i in range(len(self.bubbleSort)):
                infoListBox.insert(END, self.bubbleSort[i])
        elif selectAlg.get()=="Merge Sort":
            for i in range(len(self.mergeSort)):
                infoListBox.insert(END, self.mergeSort[i])
        elif selectAlg.get() == "Selection Sort":
            for i in range(len(self.selectionSort)):
                infoListBox.insert(END, self.selectionSort[i])
        elif selectAlg.get() == "Insertion Sort":
            for i in range(len(self.insertionSort)):
                infoListBox.insert(END, self.insertionSort[i])
        elif selectAlg.get() == "Linear Search":
            for i in range(len(self.linearSearch)):
                infoListBox.insert(END, self.insertionSort[i])
        infoListBox.see('end')
        drawAlgo.runAlgorithm(self)

    def runAlgorithm(self):
        '''
        initiate the sorting visualization process by calling the functions from algo.py
        :return: None
        '''
        stepListBox.insert(END, "Steps performed")
        global data
        if selectAlg.get() == "Bubble Sort":
            bubble(self.data, self.draw, speedLimit.get(), self.steplist, self.linklist)
            self.messagebox("Message", "Successfully sorted array using Bubble Sort")
        elif selectAlg.get() == "Merge Sort":
            merge(self.data, self.drawMerge, speedLimit.get(), self.steplist, self.linklist)
            self.messagebox("Message", "Successfully sorted array using Merge Sort")
        elif selectAlg.get() == "Selection Sort":
            selection(self.data, self.draw, speedLimit.get(), self.steplist, self.linklist)
            self.messagebox("Message", "Successfully sorted array using Selection Sort")
        elif selectAlg.get() == "Insertion Sort":
            insertion(self.data, self.draw, speedLimit.get(), self.steplist, self.linklist)
            self.messagebox("Message", "Successfully sorted array using Insertion Sort")
        elif selectAlg.get() == "Linear Search":
            index=linear_search(self.data,int(searchElement.get()), self.draw, speedLimit.get(), self.steplist, self.linklist)
            self.messagebox("Message", f"Successfully finded Element {int(searchElement.get())} at index {index}")

class DiffCodeLangs:
    '''
    in progress
    '''
    def __init__(self):
        self.tabs = Tk()
        self.tabs.title("Code")

        # frames
        self.buttonFrame = Frame(self.tabs, width=500, height=50).pack()
        self.textFrame = Frame(self.tabs, width=500).pack()

        # self.cLang = Button(self.buttonFrame,text="C",width=20,command=self.codeCLang).grid(row=0,column=0)
        self.cPlusPlus = Button(self.buttonFrame, text="C++", width=20, command=self.codePlusPlus).grid(row=0, column=1)
        self.python = Button(self.buttonFrame, text="Python", width=20).grid(row=0, column=2)
        self.java = Button(self.buttonFrame, text="Java", width=20).grid(row=0, column=3)
        print(selectAlg.get())

    def codeCLang(self):
        if selectAlg.get() == "Bubble Sort":
            self.textBox = Text(self.textFrame).grid(row=1, column=0)

    def codePlusPlus(self):
        if selectAlg.get() == "Bubble Sort":
            self.textBox = Text(self.textFrame).grid(row=1, column=0)


call = drawAlgo()
tab = DiffCodeLangs
# base layout
base_frame = Frame(sort, width=1600, height=300, bg="#00A6FF")
base_frame.grid(row=0, column=0, padx=10, pady=5)
baseCanvas = Canvas(sort, width=1510, height=430, bg="#D8DADA")
baseCanvas.grid(row=1, column=0, padx=10, pady=5)

short = Frame(sort, width=380, height=280,bg='orange')
short.place(x=10, y=530)
step = Frame(sort, width=745, height=280,bg = 'black')
step.place(x=400, y=530)
link = Frame(sort, width=370, height=280, bg = 'sky blue')
link.place(x=1155, y=530)

# user interface
# row0
Label(base_frame, text="Algorithm", bg="#00A6FF").grid(row=0, column=0, padx=5, pady=5, sticky=W)
algMenu = ttk.Combobox(base_frame, textvariable=selectAlg, values=["Bubble Sort", "Merge Sort","Selection Sort","Insertion Sort","Linear Search"], width=17)
algMenu.grid(row=0, column=1, padx=5, pady=5)
algMenu.current(0)

Button(base_frame, text="Generate array", bg="sky blue", width=20, command=call.showDataSet).grid(row=0, column=3,padx=5,pady=5, sticky=W)
Button(base_frame, text="Run", bg="sky blue", width=20, command=call.runAll).grid(row=0, column=4, padx=5, pady=5,sticky=W)
Button(base_frame, text="Code", bg="sky blue", width=20, command=tab).grid(row=0, column=5, padx=5, pady=5,sticky=W)

# Button(, text="Run", bg="sky blue", width=20, command=call.runAll).grid(row=0, column=4, padx=5, pady=5,sticky=W)

# row1
Label(base_frame, text="Size", bg="#00A6FF").grid(row=1, column=0, padx=5, pady=5, sticky=W)
sizeEntry = Entry(base_frame)
sizeEntry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

Label(base_frame, text="Minimum Value", bg="#00A6FF").grid(row=1, column=3, padx=5, pady=5, sticky=W)
minEntry = Entry(base_frame)
minEntry.grid(row=1, column=4, padx=5, pady=5, sticky=W)

Label(base_frame, text="Maximum value", bg="#00A6FF").grid(row=1, column=5, padx=5, pady=5, sticky=W)
maxEntry = Entry(base_frame)
maxEntry.grid(row=1, column=6, padx=5, pady=5, sticky=W)

Label(base_frame, text="Speed", bg="#00A6FF").grid(row=1, column=7, padx=5, pady=5, sticky=W)
speedLimit = Entry(base_frame)
speedLimit.grid(row=1, column=8, padx=5, pady=5, sticky=W)

Label(base_frame, text="Element", bg="#00A6FF").grid(row=0, column=6, padx=5, pady=5, sticky=W)
searchElement = Entry(base_frame)
searchElement.grid(row=0, column=7, padx=5, pady=5, sticky=W)

# listbox and Scroll Bar
infoScrollbar = Scrollbar(short)
infoScrollbar.pack(side=RIGHT,fill = Y)
infoListBox = Listbox(short, width=45, height=16, font=("Verdana", 10),yscrollcommand= infoScrollbar.set)
infoListBox.pack(side = LEFT,fill =BOTH)
infoScrollbar.config(command=infoListBox.yview)

stepScrollbar = Scrollbar(step)
stepScrollbar.pack(side=RIGHT,fill = Y)
stepListBox = Listbox(step, width= 91, height=16, font=("Verdana", 10),yscrollcommand=stepScrollbar.set)
stepListBox.pack(side= LEFT,fill=BOTH)
stepScrollbar.config(command=stepListBox.yview)

linkScrollbar = Scrollbar(link)
linkScrollbar.pack(side= RIGHT,fill = Y)
linkListBox = Listbox(link, width=44, height=16, font=("Verdana", 10),yscrollcommand=linkScrollbar)
linkListBox.pack(side=LEFT,fill=BOTH)
linkScrollbar.config(command=linkListBox.yview)

sort.mainloop()
