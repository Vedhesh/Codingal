from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x100")
root.title("Age Calculator")

def calc():
    val = entry.get()
    cel = 2025-int(val)
    messagebox.showinfo("Your age", f"{cel} year(s) old")

guide = Label(text="Birth Year")
entry = Entry(master=root)
button = Button(master=root, text="Calculate", command=calc)



guide.pack()
entry.pack()
button.pack()

root.mainloop()