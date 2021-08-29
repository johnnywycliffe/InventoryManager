# Inventory sorter GUI
# Author: Jeremy Stintzcum
# Rev: 1.0.0
# Last modified: 26AUG2021
# License: MIT
"""
Copyright 2021 Jeremy Stintzcum

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import inventory

helpText = """\
HOW TO USE:
1) Press start
2) Scan a bin
3) Scan all items in bin
4) Repeat 2 and 3 as necessary
5) When done, press create CSV

If an item is missed, re-scan bin and scan only the missed items

Press Exit to quit"""

parse = inventory.Parser()

# Button Behavior===============================================================
def startFunc():
    #Reconfigure active elements
    scrBox.configure(state='normal')
    create.configure(state='normal')
    start.configure(state="disabled")
    help.configure(state="disabled")
    #Move cursor to text box
    scrBox.focus()
    #Delete any old text
    scrBox.delete(1.0,tk.END)

def helpFunc():
    #enable box to insert text
    scrBox.configure(state='normal')
    #Insert text
    scrBox.insert(tk.INSERT,helpText)
    #Disable
    scrBox.configure(state='disabled')

def createFunc():
    #Retrieve data from textbox
    data = scrBox.get('1.0','end-1c')
    fileName = filename.get()
    #Give data to parser
    parse.batchParse(fileName,data)
    #Clean up and reset
    scrBox.delete(1.0,tk.END)
    scrBox.configure(state='disabled')
    create.configure(state='disabled')
    start.configure(state="normal")
    help.configure(state="normal")
    start.focus()

def exit():
    win.destroy()

# GUI===========================================================================
#Init Window
win = tk.Tk() # Create window
win.title("Inventory CSV Maker") #Set title of window

#initialize GUI elements
#Frames
fileNameFrame = ttk.LabelFrame(win, text="File Name")
#Vars
filename = tk.StringVar()
#Labels
scrBoxLbl = ttk.Label(win, text="Input area")
fileNameLbl = ttk.Label(fileNameFrame, text="Enter file name")
#Text entry
fileNameBox = ttk.Entry(fileNameFrame, width=20, textvariable=filename)
#Buttons
start = ttk.Button(win, text="Start",command=startFunc)
create = ttk.Button(win, text="Create CSV",command=createFunc)
help = ttk.Button(win, text="Help",command=helpFunc)
exit = ttk.Button(win, text="Exit",command=exit)
#Scroll Box
scrBox = scrolledtext.ScrolledText(win,width=30,height=12,wrap=tk.WORD)

#Set up grid
scrBoxLbl.grid(column=0,row=0,pady=8)
scrBox.grid(column=0,row=1,rowspan=4, padx=8,pady=8)
start.grid(column=1, row=1, padx=8)
create.grid(column=1, row=2, padx=8)
help.grid(column=1, row=3, padx=8)
exit.grid(column=1, row=4, padx=8)
fileNameFrame.grid(column=0, row=6, padx=8, pady=8, columnspan=2)
fileNameBox.grid(column=1,row=0,sticky="W", padx=8, pady=8)
fileNameLbl.grid(column=0,row=0,sticky="W", padx=8, pady=8)

#Disable certain buttons at start
scrBox.configure(state='disabled')
create.configure(state='disabled')

# RUN===========================================================================
#Start GUI
win.mainloop()

