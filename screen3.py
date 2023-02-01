from tkinter import *
import comps.GuinessPro

class Screen3:
    def __init__(self, master):
        self.master = master
        self.master.geometry('500x470')
        self.master.title('COMPETITIONS /// Jack Gill - Project')
        self.label = Label(self.master, text='COMPETITIONS', font=('Verdana', 14)).grid(row=0, column=1, columnspan=3)
        self.button1 = Button(self.master, text='BACK', command=self.master.destroy).grid(row=1, column=1)

        # buttons
        self.button1 = Button(self.master, text = 'Guiness Pro Series', command = self.printGuinPro, height = 2, width = 11).grid(row = 1, column = 1)

        self.quitButton = Button(self.master, text = 'BACK',  command = self.master.destroy, height = 2, width = 11).grid(row = 5, column = 1, columnspan =2)

        self.output_box = Text(self.master, width=70, height=20, bg='light blue', wrap = WORD)
        self.output_box.grid(row=4, column=1, columnspan =2, sticky=W)

    def printGuinPro(self):
        self.output_box.delete(0.0, END)
        res = comps.GuinessPro.printResults()
        self.output_box.insert(0.0, res)
