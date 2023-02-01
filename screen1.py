from tkinter import *
from clubTeams import *
import clubTeams.Ulster.UlsSquad
import clubTeams.Leinster.LeinSquad
import clubTeams.Connacht.ConSquad
import clubTeams.Munster.MunSquad
baseLocation = "/Users/jackgill/Desktop/CompProjProgram/clubTeams"

class Screen1:
    def __init__(self, master):
        self.master = master
        self.master.geometry('430x470')
        self.master.title('CLUB TEAMS /// Jack Gill - Project')
        self.label = Label(self.master, text='CLUB TEAMS', font=('Verdana', 14)).grid(row=0, column=1, columnspan=3)
        self.button1 = Button(self.master, text='BACK', command=self.master.destroy).grid(row=1, column=1)

        # buttons
        self.quitButton = Button(self.master, text = 'BACK',  command = self.master.destroy, height = 2, width = 11).grid(row = 5, column = 1, columnspan =2)  

        self.button1 = Button(self.master, text = 'Ulster', command = self.printULS, height = 2, width = 11).grid(row = 1, column = 1)
        self.button2 = Button(self.master, text = 'Connacht', command = self.printCON,height = 2, width = 11).grid(row = 1, column = 2)
        self.button3 = Button(self.master, text = 'Leinster', command = self.printLEIN,height = 2, width = 11).grid(row = 2, column = 1)
        self.button4 = Button(self.master, text = 'Munster',  command = self.printMUN,height = 2, width = 11).grid(row = 2, column = 2)

        self.output_box = Text(self.master, width=60, height=20, bg='light blue', wrap = WORD)
        self.output_box.grid(row=4, column=1, columnspan =2, sticky=W)


    def printULS(self):
        self.output_box.delete(0.0, END)
        res = clubTeams.Ulster.UlsSquad.printSquad()
        self.output_box.insert(0.0, res)
        

    def printCON(self):
        self.output_box.delete(0.0, END)
        res = clubTeams.Connacht.ConSquad.printSquad()
        self.output_box.insert(0.0, res)

    def printLEIN(self):
        self.output_box.delete(0.0, END)
        res = clubTeams.Leinster.LeinSquad.printSquad()
        self.output_box.insert(0.0, res)
        
    def printMUN(self):
        self.output_box.delete(0.0, END)
        res = clubTeams.Munster.MunSquad.printSquad()
        self.output_box.insert(0.0, res)


def main():
    root = Tk()
    Menu(root)
    root.mainloop()
if __name__ == '__main__':
    main()