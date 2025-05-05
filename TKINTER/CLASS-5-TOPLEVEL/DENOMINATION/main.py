from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.geometry("650x400")
root.title("Denomination New")
root.configure(bg="light blue")

upload = Image.open("TKINTER\CLASS-5-TOPLEVEL\DENOMINATION\\fixed_alpha.png")
upload.thumbnail((300, 300))

image = ImageTk.PhotoImage(upload)

label = Label(master=root, image=image, bg="light blue")
label1 = Label(master=root, text="Hey User, Welcome to Denomination Calculator [UPDATED].", bg="light blue")

label.place(x=180, y=20)
label1.place(relx=0.5, y=340, anchor=CENTER)






root.mainloop()