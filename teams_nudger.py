#!/usr/bin/env python3
# Written by: Abhigyan Kumar

import pyautogui as autogui

from datetime import datetime as dt
from time import sleep
from os import system


"""
TBD/Issues: 
1. Find a more elegant solution, overall.
2. This still causes a python window to be popped up in FOREGROUND to be effective.
3. Get the top left and bottom right max possiblities dynamically. 
"""

autogui.FAILSAFE = False  # prevent the double shake exit.
format_time = "%H:%M:%S"
count = 1    
flag_for_main = True
total_count_to_wait = int(150/20)

def fun():  # shake arount the mouse.
    x,y = autogui.position()
    autogui.moveTo(1000, 510, .3, autogui.easeInBounce) 
    autogui.moveTo(50, 50, .2, autogui.easeInBounce) 
    autogui.moveTo(x,y,1,autogui.easeInBounce)


def tick(cur_time):  # One sleep cycle.
    print(cur_time.strftime(format_time))
    sleep(20)


# Main loop.
# First launch: shake the mouse and hten go into waiting stage.
while(flag_for_main):
    system('cls')
    print("Started execution")
    print("Count:",count)
    fun()
    # sleep(150)    # Wasn't really informative and lead to confusion.
    for i in range(total_count_to_wait):
        tick(dt.now())
    print("completed a nudge to prevent away status! :D\n Waiting for timeout ")
    count += 1
