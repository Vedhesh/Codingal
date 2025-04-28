from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x100")
root.title("in to cm")

def show():
    inc = entry.get()
    cm = float(inc)*2.54
    messagebox.showinfo("Result", f"{cm}cm")

guide = Label(master=root, text="Enter Inches")
entry = Entry(master=root)
button = Button(master=root, text="Convert", command=show)

guide.pack()
entry.pack()
button.pack()

root.mainloop()

