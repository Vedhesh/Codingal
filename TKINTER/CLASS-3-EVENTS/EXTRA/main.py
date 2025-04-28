from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x100")
root.title("Temp Converter")

def calc():
    val = entry.get()
    cel = ((int(val)-32)*5/9)//1
    messagebox.showinfo("Result", f"{cel}◦")

guide = Label(text="F◦ to C◦")
entry = Entry(master=root)
button = Button(master=root, text="Calculate", command=calc)



guide.pack()
entry.pack()
button.pack()

root.mainloop()