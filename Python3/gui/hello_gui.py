# -*- coding:utf-8 -*-
#! /bin/env python3 

__author__ = 'weekend27'

# a Python GUI module

from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text="Hello, Python!")
        self.helloLabel.pack()
        self.quitButton = Button(self, text="Quit", command=self.quit)
        self.quitButton.pack()

app = Application()
app.master.title('Hello Python')
app.mainloop()
