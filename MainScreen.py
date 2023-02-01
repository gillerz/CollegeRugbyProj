from tkinter import *; import screen1; import screen2; import screen3; import screen4; 

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.geometry('280x170')
        self.master.title('MAIN SCREEN /// Jack Gill - Project')  # text on the top of the window bar
        self.label = Label(self.master, text = 'RUGGER', font = ('Arial', 20, "bold italic")).grid(row = 0, column = 1, columnspan = 2) # title for the app
        # buttons
        self.button1 = Button(self.master, text = 'CLUB TEAMS', command = self.screen1, height = 2, width = 11).grid(row = 1, column = 1)
        self.button2 = Button(self.master, text = 'PLAYERS', command = self.screen2, height = 2, width = 11).grid(row = 1, column = 2)
        self.button3 = Button(self.master, text = 'COMPS', command = self.screen3, height = 2, width = 11).grid(row = 2, column = 1)
        self.button4 = Button(self.master, text = 'INTERNATIONAL TEAMS', command = self.screen4,  height = 2, width = 11).grid(row = 2, column = 2)
        self.quitButton = Button(self.master, text = 'QUIT',  command = self.master.destroy, height = 2, width = 11).grid(row = 5, column = 1, columnspan =2)        

    # Screen1 is for CLB TEAMS page
    def screen1(self):  
        root1 = Toplevel(self.master)
        screen1.Screen1(root1)
    # Screen2 is for PLAYERS page
    def screen2(self):
        root2 = Toplevel(self.master)
        screen2.Screen2(root2)
    # Screen3 is for COMPS page
    def screen3(self):
        root3 = Toplevel(self.master)
        screen3.Screen3(root3)
    # Screen4 is for INT TEAMS page
    def screen4(self):
        root4 = Toplevel(self.master)
        screen4.Screen4(root4)

def main():
    root = Tk()
    Menu(root)
    root.mainloop()
if __name__ == '__main__':
    main()