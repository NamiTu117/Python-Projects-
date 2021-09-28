import tkinter as tk 
from tkinter import *



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
        
        #label text 
        self.lblGene = Label(self.master, text='Text Generator', font=("Helvetica", 16), fg='white', bg='black')
        self.lblGene.place(x=25.5,y=25.5, anchor=CENTER)
        
        #creating text box
        self.txtGene = Entry(self.master, text=self.varGene,font=("Helvetica", 16), fg='black',bg='white')
        self.txtGene.place(relx=0.5, rely=0.5, anchor=CENTER)

        #create submit button
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command= self.submit )
        self.btnSubmit.place(relx = 1, rely= 1, anchor=CENTER)
        


    def submit(self):
        text = self.varGene.get()
        self.lblDisplay.config(text='{}'.format(text))


        
    


#function that runs window 
if __name__ == "__main__":
    root = Tk()
    App = Gen(root)
    root.mainloop()
