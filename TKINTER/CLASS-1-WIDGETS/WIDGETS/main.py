from tkinter import *
from datetime import date
root = Tk()
root.title("Lazy Reply")

text_area = Text(height=20)
def display():
    name = entry.get()
    user = entry2.get()
    text_area.delete(END)
    text_area.insert(END, f"Hello {name} this message is to acknowledge your existence\n Handwritten by me. \n from {user} - {date.today()}.")

welcome = Label(text="Welcome message maker tool Version 1.0", fg="white",bg="blue", width=100)
guide = Label(text="Enter the candidate's Full name:", fg="gray", width=100)
entry = Entry(width=60)
guide2 = Label(text="Enter the sender's Full name:", fg="gray", width=100)
entry2 = Entry(width=60)
button = Button(text="Formulate the message", command=display, bg="skyblue")



welcome.pack()
guide.pack()
entry.pack()
guide2.pack()
entry2.pack()
text_area.pack()
button.pack(pady=10)
root.mainloop()