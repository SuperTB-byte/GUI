# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 16:17:59 2020

@author: Thong
"""
from tkinter import *
import random as r
import time
#creating the window or root widget

root = Tk()
root.title("Rock, Paper, Scissor!")
click = True

#LABELS AND BUTTONS
myLabel=Label(root,text="Let's play Rock, Paper, Scissor!")
b1 = Button(root,text="Rock",
            command=lambda:youPick('rock'))
b2 = Button(root,text="Paper",
            command=lambda:youPick('paper'))
b3 = Button(root,text="Scissor",
            command=lambda:youPick('scissor'))

c1= Label(root,text="rock")
c2= Label(root,text="paper")
c3= Label(root,text="scissor")

w= Label(root,text="You win")
l= Label(root,text="You lose")  
d= Label(root,text="You draw")

#shove into the screen
myLabel.pack()
b1.pack()
b2.pack()
b3.pack()

#creat an event loop

def play():
    global b1,b2,b3,c1,c2,c3
    
def computerPick():
    choice=r.choice(["rock", "paper", "scissor"])
    return choice
    
def youPick(yourChoice):   
    global click
    
    compPick = computerPick()
    
    if click == True:
        if yourChoice == 'rock' and compPick == 'rock':
            d.pack()
            click == False
            d.after(2000, d.pack_forget)
            
        elif compPick == 'paper':
            l.pack()
            click == False
            l.after(2000, l.pack_forget)
            
        else:
            w.pack()
            click == False
            w.after(2000, w.pack_forget)
            
            #ONLY PRINTS ONCE OF EACH CONDITION
root.mainloop()
