import tkinter

class Gui(Frame):
    def createwidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.LOGIN = Button(self)
        self.LOGIN["text"] = "LOGIN"
        self.LOGIN["fg"] = "blue"
        self.LOGIN["command"] = self.quit
