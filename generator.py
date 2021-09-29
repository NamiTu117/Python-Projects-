import tkinter as tk 
from tkinter import *
import webbrowser 

import WebAssignment

#creating window and function
class Gen(Frame):
    def __init__(self,master):
        Frame.__init__(self)



        #creating generator form
        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700,400))
        self.master.title('Text Generator')
        self.master.config(bg='black')

        self.varGene = StringVar()
        self.varGene = StringVar()

        #lines up widgets
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        
        #these specific placements center widgets 
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)
        
        #label text 
        self.lblGene = Label(self.master, text='Text Generator', font=("Helvetica", 16), fg='white', bg='black')
        self.lblGene.grid(row=0, column=2)
        
        
        #creating text box
        self.txtGene = Entry(self.master, text=self.varGene,font=("Helvetica", 16), fg='black',bg='white')
        self.txtGene.grid(row=1,column=2)
        
        

        #create submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command= self.submit )
        self.btnSubmit.grid(row=2, column=2)
        
        


    def submit(self):
        usertext = self.varGene.get()
        text1 = ''' 
<html>
    <body>
        <h1>
            '''
       
        text2 = '''
        </h1>
    </body>
</html>
     '''
        websitetext = text1 + usertext + text2 
        self.lblGene.config(text=' {} '.format(usertext))

        #opens new html file 
        file = open("assignment.html", "w")
        file.write(websitetext)
        file.close()

        webbrowser.open_new_tab("assignment.html")

     


#function that runs window 
if __name__ == "__main__":
    root = Tk()
    App = Gen(root)
    root.mainloop()
