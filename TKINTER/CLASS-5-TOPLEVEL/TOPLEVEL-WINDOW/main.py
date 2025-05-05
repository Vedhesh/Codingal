from tkinter import *

root = Tk()
root.geometry("300x300")
root.title("root")

def open():
    new = Toplevel()
    new.geometry("200x200")
    new.title("toplevel")

    guide2 = Label(master=new, text="Toplevel window")

    guide2.pack()

    new.mainloop()


guide = Label(master=root, text="Root window")
button = Button(master=root, text="Open Toplevel", command=open)

guide.pack()
button.pack()

root.mainloop()