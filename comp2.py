from tkinter import *
import tkinter as tk
from methods import *
from menu import *
import threading

class ApplicationC:
    
    def __init__(self, master=None):
        self.standardFont  = ("Arial", "10")
        self.standardShow = ("Arial", "9", "bold")
        
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()
        
        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 5
        self.secondContainer.pack()
            
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
        
        self.title = Label(self.firstContainer, text="Methods Computational")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()
        
        self.integerLabel = Label(self.secondContainer, text="Integer:", font=self.standardFont)
        self.integerLabel.pack()
        
        self.integer = Entry(self.secondContainer)
        self.integer["width"] = 15
        self.integer["font"] = self.standardFont
        self.integer.pack(side=LEFT)
        
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
        
        
        self.msgInteger = Label(self.fourthContainer, text="", font=self.standardShow)
        self.msgInteger.pack()
        
        self.msgBinary = Label(self.fourthContainer, text="", font=self.standardShow)
        self.msgBinary.pack()
        
    def authenticateStart(self):
        
        interger = self.integer.get()
        binary = self.binary.get()
        
        if(interger != ""):
            convertInteger = Comp2Converter()
            valueI = convertInteger.runDB(int(interger))
            self.msgInteger["text"] = valueI
        else:
            self.msgInteger["text"] = "No pass value"
            
        if(binary != ""):
            convertBinary = Comp2Converter()
            valueB = convertBinary.runBD(binary)
            self.msgBinary["text"] = str(valueB)
        else:
            self.msgBinary["text"] = "No pass value"

    def backInterface(self):
        thread_one = threading.Thread(target=root.destroy())
        thread_two = threading.Thread(target=runS())
        thread_one.start();
        thread_two.start();
        
    @staticmethod
    def runC():
        global root
        root = Tk()
        ApplicationC(root)
        root.mainloop()
    