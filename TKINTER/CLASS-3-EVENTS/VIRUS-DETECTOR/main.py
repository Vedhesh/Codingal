from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Prank")
root.geometry("200x200")

def warn():
    messagebox.showerror("Windows Defender", "14 Virus(s) are installed!")

button = Button(master=root, text="Show Prank", command=warn)
button.place(x=80, y=40)

root.mainloop()
