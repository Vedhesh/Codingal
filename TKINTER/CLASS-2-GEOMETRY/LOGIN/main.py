from tkinter import *

root = Tk()
root.title("Login")
root.geometry("400x400")

frame = Frame(master=root, width=360, height=200, bg="#d0efff")

lbl1 = Label(text="Real Name", bg="#3895d3", fg="white", width=12)
lbl2 = Label(text="Username", bg="#3895d3", fg="white", width=12)
lbl3 = Label(text="Password", bg="#3895d3", fg="white", width=12)

ent1 = Entry(root) 
ent2 = Entry(root) 
ent3 = Entry(root, show="▪") 

textbox = Text(bg="#BEBEBE", fg="black")

def display():
    name = ent1.get()
    greet = "Hey there, " + name
    message = "\nCongratulations on your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

btn = Button(text="Create New Account", command=display, bg="red")#

frame.place(x=20, y=0)
lbl1.place(x=20,y=20)
ent1.place(x=150,y=20)
lbl2.place(x=20,y=80)
ent2.place(x=150,y=80)
lbl3.place(x=20,y=140)
ent3.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(y=250)

root.mainloop()