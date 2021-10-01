import tkinter as Tk
from tkinter import filedialog as fd
from tkinter import *
import os
import datetime
from datetime import datetime, timedelta
import shutil 


#create window
class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(False, False)
        self.master.geometry('{}x{}'.format(500, 199))
        self.master.title('File Search')
        self.master.config(bg='lightgrey')

        self.varSearch = StringVar()
        self.varSearch = StringVar()
        
        #label
        self.lblSearch = Label(self.master, text='Browse', font=("Times", 12), fg='black', bg='lightgrey')
        self.lblSearch.grid(row=0, column=0, padx=(20,0), pady=(10,0))
        #button
        self.btnSearch = Button(self.master, text="Browse", width=10, height=2, command= lambda: self.search())
        self.btnSearch.grid(row=2, column=1, padx=(0,0), pady=(30,0), stick =NE)

        #button
        self.btnSearch2 = Button(self.master, text="Browse", width=10, height=2, command= lambda: self.search2() )
        self.btnSearch2.grid(row=2, column=2, padx=(0,0), pady=(30,0), stick =NE)

        #button
        self.btnTransfer = Button(self.master, text="Transfer", width=10, height=2, command= lambda: self.movefiles() )
        self.btnTransfer.grid(row=2, column=3, padx=(0,0), pady=(30,0), stick =NE)



        
        self.lblSearch = Label(self.master, text='Check Files', font=("Times", 12), fg='black', bg='lightgrey')
        self.lblSearch.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        #display
        self.lblDisplay = Label(self.master, text='', font=("Times", 12), fg='black', bg='lightgrey')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
   
        #text box 
        self.txtSearch = Entry(self.master,font=("Times", 12), fg='black',bg='lightgrey')
        self.txtSearch.grid(row=0, column=1, padx=(20,0), pady=(10,0))

        self.txtSearch2 = Entry(self.master,font=("Times", 12), fg='black',bg='lightgrey')
        self.txtSearch2.grid(row=1, column=1, padx=(30,0), pady=(30,0))

    def search(self):
        src = filedialog.askdirectory()
        self.txtSearch.delete(0,END)
        self.txtSearch.insert(0,src)

    def search2(self):
        sia = filedialog.askdirectory()
        self.txtSearch2.delete(0,END)
        self.txtSearch2.insert(0,sia)

    def movefiles(self):
        
        #set where the source of the files are
        source = self.txtSearch.get()

        #set the destination path to folder B
        destination = self.txtSearch2.get()
        files = os.listdir(source)


        for i in files:
            
            now = datetime.now()
            time = now.strftime("%H:%M:%S")
            bonk = '24:00:00' 
            if i > bonk: 
            #we are saying move the files represented by 'i' to their new destination
                shutil.move(source+"/"+i, destination)
                



if __name__ == "__main__":
    root = Tk()
    App = Search(root)
    root.mainloop()
