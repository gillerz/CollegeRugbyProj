from tkinter import *
import players.rKearney
import players.cHealy
import players.jSexton

class Screen2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('330x430')
        self.master.title('PLAYERS /// Jack Gill - Project')
        self.label = Label(self.master, text='PLAYERS', font=('Verdana', 14)).grid(row=0, column=1, columnspan=3)
        self.button1 = Button(self.master, text='BACK', command=self.master.destroy).grid(row=1, column=1)

        # buttons
        self.button1 = Button(self.master, text = 'Rob Kearney', command = self.printrKearney, height = 2, width = 11).grid(row = 1, column = 1)
        self.button2 = Button(self.master, text = 'Cian Healy', command = self.printcHealy, height = 2, width = 11).grid(row = 1, column = 2)
        self.button3 = Button(self.master, text = 'Johnny Sexton', command = self.printjSexton, height = 2, width = 11).grid(row = 2, column = 1)
        self.quitButton = Button(self.master, text = 'BACK',  command = self.master.destroy, height = 2, width = 11).grid(row = 5, column = 1, columnspan =2)
        self.output_box = Text(self.master, width=25, height=17, bg='light blue', wrap = WORD)
        self.output_box.grid(row=4, column=1, columnspan =2, sticky=W)

    def printrKearney(self):
        self.output_box.delete(0.0, END)
        res = players.rKearney.printStats()
        self.output_box.insert(0.0, res)

    def printcHealy(self):
        self.output_box.delete(0.0, END)
        res = players.cHealy.printStats()
        self.output_box.insert(0.0, res)

    def printjSexton(self):
        self.output_box.delete(0.0, END)
        res = players.jSexton.printStats()
        self.output_box.insert(0.0, res)

def main():
    root = Tk()
    Menu(root)
    root.mainloop()
if __name__ == '__main__':
    main()