# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:51:47 2020

@author: Thong
"""
#Clock

seconds = 57
minutes = 59
hours = 2

#Import time for the time.sleep(x) function
import time
day = input ("am/pm: ")
Usertime = input ("input hours:minutes:seconds => ")


#GUI 
from turtle import *
setup()
tl = Turtle()

#creating the time loops
while True:
    tl.clear()
    if day == "am":
        tl.write (str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2) + " " + "am") 
        seconds += 1
        time.sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0

    elif day == "pm":
        tl.write (str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2) + " " + "pm") 
        seconds += 1
        time.sleep(1)
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0


                            
                        
                    
    


