from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x200")
root.title("Strength Check")

def calc():
    val = len(entry.get())
    if val<=3:
        guide2.configure(text="WEAK")
        guide2.configure(fg="red")
    elif val<=5:
        guide2.configure(text="MEDIUM")
        guide2.configure(fg="orange")
    elif val<=12:
        guide2.configure(text="OK")
        guide2.configure(fg="yellow")
    elif val<=20:
        guide2.configure(text="STRONG")
        guide2.configure(fg="lime")
    elif val>=100 and val<1000:
        guide2.configure(text="GLORIOUS")   #EASTER EGG
        guide2.configure(fg="purple")
    elif val>=1000:
        guide2.configure(text="IMPOSSIBLE") #EASTER EGG
        guide2.configure(fg="blue")
def show():
    entry.configure(show="")
    showbutton.configure(state="disabled")
    showbutton.configure(text="X")

guide = Label(text="Enter a password")
guide2 = Label(text="NONE", font="Helvetica 64", bg="black", fg="white")
entry = Entry(master=root, show="·", font="Helvetica 32")
frame = Frame()
button = Button(master=frame, text="Calculate", command=calc, font="Helvetica 20")
showbutton = Button(master=frame, text="👁", command=show, state="active", font="Helvetica 20")


guide.pack()
entry.pack()
showbutton.pack(side=LEFT)
button.pack(side=RIGHT)
frame.pack(pady=1)
guide2.pack()

root.mainloop()