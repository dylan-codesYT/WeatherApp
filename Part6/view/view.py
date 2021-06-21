import tkinter
from tkinter.constants import *
from tkinter import StringVar, IntVar
from tkinter.ttk import *


class View(tkinter.Tk):

    def __init__(self, controller):
        super().__init__()
        self.geometry("700x500")

        self.controller = controller
        self.bind('<Return>', self.controller.handleButtonSearch)

        #---- Variables ----
        self.varSearch = StringVar()
        self.varTemp = StringVar()
        self.varLocation = StringVar()
        self.varCondition = StringVar()
        self.varFeelsLike = StringVar()
        self.varWindSpeed = StringVar()
        self.varWindDir = StringVar()
        self.varUnits = IntVar()

        self.varTemp.set("104")
        self.varLocation.set("The desert")

        #---- Frames ----
        self.mainframe = Frame(self)
        self.mainframe.pack()
        self._createFrameSearchBar()
        self._createFrameInfo()
        self._createFrameDetails()
        self._createFrameControls()

    
    def _createFrameSearchBar(self):
        self.frameSearchBar = Frame(self.mainframe)

        self.comboSearch = Combobox(self.frameSearchBar, textvariable=self.varSearch)
        buttonSearch = Button(self.frameSearchBar, text="Search", command=self.controller.handleButtonSearch)

        self.comboSearch.bind('<KeyRelease>', self.controller.handleComboSearch)

        self.comboSearch.pack(padx=10, side=LEFT)
        buttonSearch.pack(side=RIGHT)
        self.frameSearchBar.pack()


    def _createFrameInfo(self):
        self.frameInfo = Frame(self.mainframe)

        labelTemp = Label(self.frameInfo, textvariable=self.varTemp)
        labelLocation = Label(self.frameInfo, textvariable=self.varLocation)
        labelIcon = Label(self.frameInfo, text='image')

        labelTemp.pack(pady=5)
        labelLocation.pack(pady=5)
        labelIcon.pack(pady=5)
        self.frameInfo.pack()


    def _createFrameDetails(self):
        self.frameDetails = Frame(self.mainframe)

        labelConditionLeft = Label(self.frameDetails, text='Current Condition:')
        labelFeelsLikeLeft = Label(self.frameDetails, text='Feels Like:')
        labelWindSpeedLeft = Label(self.frameDetails, text='Wind Speed:')
        labelWindDirLeft = Label(self.frameDetails, text='Wind Direction:')

        labelConditionRight = Label(self.frameDetails, textvariable=self.varCondition)
        labelFeelsLikeRight = Label(self.frameDetails, textvariable=self.varFeelsLike)
        labelWindSpeedRight = Label(self.frameDetails, textvariable=self.varWindSpeed)
        labelWindDirRight = Label(self.frameDetails, textvariable=self.varWindDir)

        labelConditionLeft.grid(row=0, column=0, pady=5, sticky=W)
        labelConditionRight.grid(row=0, column=1, pady=5, sticky=E)
        labelFeelsLikeLeft.grid(row=1, column=0, pady=5, sticky=W)
        labelFeelsLikeRight.grid(row=1, column=1, pady=5, sticky=E)
        labelWindSpeedLeft.grid(row=2, column=0, pady=5, sticky=W)
        labelWindSpeedRight.grid(row=2, column=1, pady=5, sticky=E)
        labelWindDirLeft.grid(row=3, column=0, pady=5, sticky=W)
        labelWindDirRight.grid(row=3, column=1, pady=5, sticky=E)
        self.frameDetails.pack()


    def _createFrameControls(self):
        self.frameControls = Frame(self.mainframe)

        radioF = Radiobutton(self.frameControls, text='Fahrenheit', variable=self.varUnits, value=1, command=self.controller.updateGUI)
        radioC = Radiobutton(self.frameControls, text='Celcius', variable=self.varUnits, value=2, command=self.controller.updateGUI)

        radioF.invoke()

        radioF.pack(side=LEFT, padx=7.5, pady=5)
        radioC.pack(side=RIGHT, padx=7.5, pady=5)
        self.frameControls.pack()


    def main(self):
        self.mainloop()