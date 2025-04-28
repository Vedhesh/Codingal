from tkinter import *

root = Tk()

root.geometry("250x50")
root.title("Key Logger")

def handle_keys(event):
    print(event.char)

root.bind("<Key>", handle_keys)

def handle_clicks(event):
    print("Clicked!")

button = Button(master=root,text="Click!")
button.pack()

button.bind("<Button-1>", handle_clicks)

root.mainloop()