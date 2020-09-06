#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 10:57:58 2020

@author: CamellaDo
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


#create an event loop

def play():
    global b1,b2,b3,c1,c2,c3,w,l,d
    
def computerPick():
    choice=r.choice(["rock", "paper", "scissor"])
    print("Computer:"+choice)
    return choice
    
def youPick(yourChoice):   
    global click
    
    compPick = computerPick()
    
    if click == True: #ROCKchoice
        if (yourChoice == 'rock' and compPick == 'rock') or (yourChoice == 'paper' and compPick == 'paper') or (yourChoice == 'scissor' and compPick == 'scissor'):
            d.pack()
            print("You:"+yourChoice)
            print("Draw")
            click == False
            d.after(2000, d.pack_forget)
            
        elif (yourChoice == 'rock' and compPick == 'paper') or (yourChoice == 'paper' and compPick == 'scissor') or (yourChoice == 'scissor' and compPick == 'rock'):
            l.pack()
            print("You:"+yourChoice)
            print("Lose")
            click == False
            l.after(2000, l.pack_forget)
            
        else:
            w.pack()
            print("You:"+yourChoice)
            print("Win")
            click == False
            w.after(2000, w.pack_forget)
        
        return compPick
            #ONLY PRINTS ONCE OF EACH CONDITION
root.mainloop()



