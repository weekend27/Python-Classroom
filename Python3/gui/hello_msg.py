# -*- coding:utf-8 -*-
#! /bin/env python3    

__author__ = 'weekend27'

# a Python GUI module

from tkinter import *
import tkinter.messagebox as messagebox

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text="Hello", command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'Python'
        messagebox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello Python')
app.mainloop()
