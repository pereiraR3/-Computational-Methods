from tkinter import *
import tkinter as tk
from real754 import *
from comp2 import *
import threading
import subprocess

class Application:
    def __init__(self, master=None):
        self.standarFont = ("Arial", "10")
        self.extraFont = ("Arial", "10", "bold")
        
        self.widgetTitle = Frame(master)
        self.widgetTitle["pady"] = 5
        self.widgetTitle["padx"] = 10
        self.widgetTitle.pack()
        
        self.title = Label(self.widgetTitle, text="Choice:", font=self.extraFont)
        self.title["width"] = 8
        self.title.pack()
        
        self.widget1 = Frame(master)
        self.widget1["pady"] = 5
        self.widget1["padx"] = 10
        self.widget1.pack()
        
        self.widget2 = Frame(master)
        self.widget2["pady"] = 5
        self.widget2["padx"] = 10
        self.widget2.pack()
        
        self.buttonComp2 = Button(self.widget1, text="Comp2")
        self.buttonComp2["width"] = 10
        self.buttonComp2["font"] = self.standarFont
        self.buttonComp2["command"] = self.on_button_comp2
        self.buttonComp2.pack()
        
        self.buttonReal = Button(self.widget2, text="IEEE 754")
        self.buttonReal["font"] = self.standarFont
        self.buttonReal["width"] = 10
        self.buttonReal["command"] = self.on_button_real
        self.buttonReal.pack()
        
        
    def on_button_comp2(self):
        entry = ApplicationC();
        thread_one = threading.Thread(target=rootMain.destroy())
        thread_two = threading.Thread(target=entry.runC())
        thread_one.start()
        thread_two.start()
            
    def on_button_real(self):
        entry = ApplicationR();
        thread_one = threading.Thread(target=rootMain.destroy())
        thread_two = threading.Thread(target=entry.runR())
        thread_one.start()
        thread_two.start()
            

def runS():
    global rootMain
    rootMain = Tk()
    Application(rootMain)
    rootMain.mainloop()