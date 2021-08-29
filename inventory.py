# Inventory sorter
# Author: Jeremy Stintzcum
# Rev: 1.0.0
# Last modified: 26AUG2021
# License: MIT
"""
Copyright 2021 Jeremy Stintzcum

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""

import csv

version = "1.0.0"

class Bins:
    """ Objects representing each physical location
        addItem(str): put an item in the bin
        printBin(): Prints contents of bin to screen
    """
    def __init__(self, newName):
        self.name = newName
        self.items = {}
    
    def addItem(self, item):
        """ inserts item into dict or incriments if already present """
        # check if item exists in dictionary
        if item in self.items.keys():
            self.items[item] += 1
        else:
            self.items[item] = 1
            
    def printBin(self):
        """ Displays text from in to screen """
        print("Bin "+self.name+": "+str(self.items))

class Inventory:
    """ Main inventory class
        addItem(Bins,str): Creates an item inside of a bin.
        addBin(str): Adds bin to list
        printBins(): Prints the inventory to screen
        writeBins(): Writes contents of inventory to csv file 
        setFileName(str): Sets the file name to use
    """
    def __init__(self):
        self.fileName = 'inventory'
        self.binList = []
    
    def addItem(self, newBin, item):
        """ Adds item to a bin
            newBin: Bin object to put item into
            item: a string of text
        """
        #error checking
        if item is None:
            print("Invalid input - item is none")
            return
        # Add item to bin
        newBin.addItem(item)
    
    def addBin(self, name):
        """ grabs bin by name. If bin doesn't exist, adds it then returns it.
            name: string representing bin
            return: Bin object with name chosen
        """
        newBin = None
        # Check if bin already exists
        for i in self.binList:
            if i.name == name:
                newBin = i
        # If bin does not exist, create it
        if newBin == None:
            newBin = Bins(name)
            self.binList.append(newBin)
        return newBin
       
    def printBins(self):
        """ Prints current scan results to screen """
        print(self.binList)
        for i in self.binList:
            i.printBin()
    
    def writeBins(self):
        """ Writes inventory to a CSV file """
        #open CSV file, creating it if it doesn't exist
        with open(self.fileName+'.csv','w') as invFile:
            writer = csv.writer(invFile,delimiter=',')
            #Write header
            writer.writerow(["Bin","Part number","Quantity"])
            #Write each row
            for i in self.binList:
                #add a1 empty bin if needed
                if len(i.items) == 0 and i.name != "No bin provided":
                    writer.writerow([i.name,"No items provided"])
                else:
                    for j in i.items:
                        writer.writerow([i.name,j,i.items[j]])
                #Add a space
                writer.writerow([])

    def setFileName(self,name):
        """ Sets the file name to be written """
        self.fileName = name

class Parser:
    """ Handles input from the user and scanner
        batchParse(str,str): Takes in a file name and data and creates CSV
        cmdParse(): Command line parser for non-gui systems
        printHelp: Prints help dialogue for cmdParse
    """
    def __init__(self):
        #Set up necessary classes
        self.inv = Inventory()
        #Create catch bin and add to inv
        self.activeBin = self.inv.addBin("No bin provided")
   
    def batchParse(self,filename,data):
        """ Converts data to CSV
            filename: String for the filename
            data: List of items seperated by newlines
        """
        #Cut up by newline
        split = data.splitlines()
        #Sort
        for i in split:
            if i == "":
                continue
            elif i[0].isalpha():
                self.activeBin = self.inv.addBin(i)
            elif i[0].isnumeric():
                self.inv.addItem(self.activeBin,i)
            else:
                continue
        #Check filename
        if filename == "":
            filename = "inventory"
        #Send to CSV
        self.inv.setFileName(filename)
        self.inv.writeBins()
            
    def cmdParse(self):
        """ Parser for the command line """
        ended = False
        active = False
        print("Inventory Manager Ver "+version+".\nWritten by Jeremy Stintzcum, copyright 2021.\n")
        inputString = "Please enter 'Start' to begin scanning, 'Help' for help, and 'Exit' to quit program.\n"
        while not ended:
            inp = input(inputString)
            if inp == "": #Empty string
                print("Invalid input.")
            elif inp.lower() == "help": #Provides help dialogue
                self.printHelp()
            elif inp.lower() == "start": #Begins the scanner
                self.inv.setFileName(input("Enter file name:"))
                inputString = "Start by scanning a bin, then the items in that bin.\n"
                active = True
            elif inp.lower() == "exit": #exits the program
                self.inv.printBins()
                inp = input("Save file? yes/No\n") #allow users not to save files in case of junk
                if active and inp.lower()[0] == 'y':
                    self.inv.writeBins()
                ended = True
            elif inp[0].isalpha() and active: #Bins start wit a letter
                self.activeBin = self.inv.addBin(inp)
                print("Bin '"+inp+"' selected.")
                inputString = "Scan an item, or scan a different bin.\n"
            elif inp[0].isnumeric() and active: #Parts start with a number
                self.inv.addItem(self.activeBin,inp)
                print("Item '"+inp+"' was added to bin '"+self.activeBin.name+"'")
            else:
                print("Invalid input.")
    
    def printHelp(self):
        print("How to use:\n"+
            "NOTE: Ensure program is focused so scanner's input is fed to this script.\n"+
            "1) Type start, then press enter.\n"+
            "2) Enter a file name.\n"+
            "3) Scan a bin.\n"+
            "4) Scan items in bin.\n"+
            "5) Type 'exit' once all items are scanned.\n"+
            "Once exited, the file will be created in the directory this file was run in.\n\n"+
            "Scanning the same item multiple times will increase the quantity of the item.\n"+
            "If an item is missed, rescan the bin and then the missed item.\n")

# Main function
if __name__ == "__main__":
    parse = Parser()
    parse.cmdParse()
