from tkinter import *

def printer(event):
    print("Hello, world!")

root = Tk()
but = Button(root, text = "Print")
but.bind("<Button-1>", printer)
but.pack()
root.mainloop()
