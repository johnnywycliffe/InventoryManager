import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import inventory

# Button Behavior===============================================================
def startFunc():
    #Reconfigure active elements
    scrBox.configure(state='normal')
    create.configure(state='normal')
    start.configure(state="disabled")
    help.configure(state="disabled")
    
    #Move cursor to text box
    scrBox.focus()



def name_of_function():
    pass

# GUI===========================================================================
#Init Window
win = tk.Tk() # Create window
win.title("Inventory CSV Maker") #Set title of window

#initialize GUI elements
#Labels
scrBoxLbl = ttk.Label(win, text="Input area")
status = ttk.Label(win)
#Buttons
start = ttk.Button(win, text="Start",command=startFunc)
create = ttk.Button(win, text="Create CSV",command=name_of_function)
help = ttk.Button(win, text="Help",command=name_of_function)
exit = ttk.Button(win, text="Exit",command=name_of_function)
#Scroll Box
scrBox = scrolledtext.ScrolledText(win,width=30,height=12,wrap=tk.WORD)

#Set up grid
scrBoxLbl.grid(column=0,row=0)
scrBox.grid(column=0,row=1,rowspan=4)
start.grid(column=1, row=1, padx=8)
create.grid(column=1, row=2, padx=8)
help.grid(column=1, row=3, padx=8)
exit.grid(column=1, row=4, padx=8)
status.grid(column=0,row=6,columnspan=2)

#Disable certain buttons at start
scrBox.configure(state='disabled')
create.configure(state='disabled')

#Start GUI
win.mainloop()

