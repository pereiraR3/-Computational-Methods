from tkinter import *
import tkinter as tk
from methods import *
from menu import *
import subprocess
import threading

class ApplicationR:
    
    def __init__(self, master=None):
        self.standardFont  = ("Arial", "10")
        self.standardShow = ("Arial", "9", "bold")
        
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()
        
        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 5
        self.secondContainer.pack()
            
        self.extraContainer = Frame(master)
        self.extraContainer["padx"] = 5
        self.extraContainer.pack()
    
        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 5
        self.thirdContainer.pack()
        
        
        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 10
        self.fourthContainer.pack()
        
        #######################
        self.fiveContainer = Frame(master)
        self.fiveContainer["pady"]= 10
        self.fiveContainer.pack()
        #######################
        
        self.title = Label(self.firstContainer, text="IEEE754")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()
        
        self.integerReal = Label(self.secondContainer, text="Real:", font=self.standardFont)
        self.integerReal.pack()
        
        self.real = Entry(self.secondContainer)
        self.real["width"] = 15
        self.real["font"] = self.standardFont
        self.real.pack(side=LEFT)
        
        self.precision = Entry(self.extraContainer)
        self.precision["width"] = 15
        self.precision["font"] = self.standardFont
        self.precision.pack(side=LEFT)
        
        self.binaryLabel = Label(self.thirdContainer, text="Binary:", font=self.standardFont)
        self.binaryLabel.pack()
        
        self.binary = Entry(self.thirdContainer)
        self.binary["width"] = 15
        self.binary["font"] = self.standardFont
        self.binary.pack(side=LEFT)
            
            
        self.authenticate = Button(self.fourthContainer, text="Start")
        self.authenticate["font"] = self.standardFont
        self.authenticate["width"] = 10
        self.authenticate["command"] = self.authenticateStart
        self.authenticate.pack()
        
        self.back = Button(self.fourthContainer, text="Back")
        self.back["font"] = self.standardFont
        self.back["width"] = 10
        self.back["command"] = self.backInterface
        self.back.pack()
        
        self.msgReal = Label(self.fourthContainer, text="", font=self.standardShow)
        self.msgReal.pack()
        
        self.msgBinary = Label(self.fourthContainer, text="", font=self.standardShow)
        self.msgBinary.pack()
        
    def authenticateStart(self):
        
        real = self.real.get()
        binary = self.binary.get()
        precision = self.precision.get()
        
        if(binary != ""):
            convertBinary = realConvert()
            valueReal = convertBinary.runBR(binary)
            self.msgReal["text"] = str(valueReal)
        else:
            self.msgReal["text"] = "No pass value"
        if(real != ""):
            convertReal = realConvert()
            valueB = convertReal.runRB(float(real), int(precision))
            self.msgBinary["text"] = str(valueB)
        else:
            self.msgBinary["text"] = "No pass value"
            
    def backInterface(self):
        thread_one = threading.Thread(target=root.destroy())
        thread_two = threading.Thread(target=runS())
        thread_one.start();
        thread_two.start();
    
    def runR(self):
        global root
        root = Tk()
        ApplicationR(root)
        root.mainloop()
    
        