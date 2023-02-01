from tkinter import *
import intTeams.ERU
import intTeams.IRFU

class Screen4:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x470')
        self.master.title('INTERNATIONAL TEAMS/// Jack Gill - Project')
        self.label = Label(self.master, text='INTERNATIONAL TEAMS', font=('Verdana', 14)).grid(row=0, column=1, columnspan=3)
        self.button1 = Button(self.master, text='BACK', command=self.master.destroy).grid(row=1, column=1)

        # buttons
        self.button1 = Button(self.master, text = 'Ireland', command = self.printIRFU, height = 2, width = 11).grid(row = 1, column = 1)
        self.button2 = Button(self.master, text = 'England', command = self.printERU, height = 2, width = 11).grid(row = 1, column = 2)


        self.quitButton = Button(self.master, text = 'BACK',  command = self.master.destroy, height = 2, width = 11).grid(row = 5, column = 1, columnspan =2)
        
        self.output_box = Text(self.master, width=110, height=20, bg='light blue', wrap = WORD)
        self.output_box.grid(row=4, column=1, columnspan =2, sticky=W)

    def printIRFU(self):
        self.output_box.delete(0.0, END)
        res = intTeams.IRFU.printSquad()
        self.output_box.insert(0.0, res)

    def printERU(self):
        self.output_box.delete(0.0, END)
        res = intTeams.ERU.printSquad()
        self.output_box.insert(0.0, res)