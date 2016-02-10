#GUI layout basics

from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    root.geometry("640x480+400+400")
    content = Major(root)
    root.mainloop()

def gquit():
    quit()

class Major(Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Blackbird poops")

        self.frame1 = ttk.Frame(self, borderwidth=2, relief="sunken")

        self.onevar = BooleanVar()
        self.twovar = BooleanVar()
        self.threevar = BooleanVar()

        self.onevar.set(True)
        self.twovar.set(False)
        self.threevar.set(True)

        self.namelbl = ttk.Label(self.frame1, text="Name")
        self.name = ttk.Entry(self.frame1)
        self.one = ttk.Checkbutton(self.frame1, text="One", variable=self.onevar, onvalue=True)
        self.two = ttk.Checkbutton(self.frame1, text="Two", variable=self.twovar, onvalue=True)
        self.three = ttk.Checkbutton(self.frame1, text="Three", variable=self.threevar, onvalue=True)
        self.ok = ttk.Button(self, text="Okay")
        self.quitB = ttk.Button(self, text="Quit", command=gquit)

        self.grid(column=0, row=0, sticky=(N, S, E, W))

        self.frame1.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
        self.namelbl.grid(column=0, row=0, columnspan=2, sticky=(W))
        self.name.grid(column=0, row=1, columnspan=2, sticky=(N, E, W))

        self.one.grid(column=0, row=3)
        self.two.grid(column=1, row=3)
        self.three.grid(column=2, row=3)
        self.ok.grid(column=0, row=0, sticky=(N, W), padx=5, pady=5)
        self.quitB.grid(column=0, row=1, sticky=(N, W), padx=5)

        self.parent.columnconfigure(0, weight=1)
        self.parent.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=1)
        self.rowconfigure(1, weight=1)

        for child in self.frame1.winfo_children(): child.grid_configure(padx=5, pady=5)


if __name__ == '__main__':
    main()
