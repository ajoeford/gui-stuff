
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("640x480+400+400")

def gquit():
    quit()

#Change to classes
content = ttk.Frame(root, padding=(3,3,12,12))
frame1 = ttk.Frame(content, borderwidth=2, relief="sunken")

onevar= BooleanVar()
twovar= BooleanVar()
threevar= BooleanVar()

onevar.set(True)
twovar.set(False)
threevar.set(True)

namelbl = ttk.Label(frame1, text="Name")
name = ttk.Entry(frame1)
one = ttk.Checkbutton(frame1, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(frame1, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(frame1, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
quitB = ttk.Button(content, text="Quit", command=gquit)

content.grid(column=0, row=0, sticky=(N, S, E, W))

frame1.grid(column=1, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=0, row=0, columnspan=2, sticky=(W))
name.grid(column=0, row=1, columnspan=2, sticky=(N, E, W))

one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=0, row=0, sticky=(N, W), padx=5)
quitB.grid(column=0, row=1, sticky=(N, W), padx=5, pady=5)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=0)
content.columnconfigure(1, weight=0)
content.columnconfigure(2, weight=0)
content.columnconfigure(3, weight=1)
content.rowconfigure(1, weight=1)

for child in frame1.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()
