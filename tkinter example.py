# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 14:39:00 2020

@author: Thong
"""

from tkinter import *

#creating the window or root widget

root = Tk()


#creating the label widget
myLabel = Label(root, text="Hello world!")


#shove into the screen
myLabel.pack()

#creat an event loop

root.mainloop()
