from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x300")
root.title("Interest Calculator")

def calc():
    p = int(entry1.get())
    r = int(entry2.get())
    t = int(entry2.get())
    sim = p+(p*r*t/100)
    com = p*(1+(r/100))**t
    text.delete('1.0', END)
    text.insert(END, f"Analysis")
    text.insert(END, "\n\n----Simple Insterest----")
    text.insert(END, f"\n\tEnd Value : {sim}")
    text.insert(END, f"\n\tDifference: {sim-p}")

    text.insert(END, "\n\n---Compound Insterest---")
    text.insert(END, f"\n\tEnd Value : {com}")
    text.insert(END, f"\n\tDifference: {com-p}")

    text.insert(END, "\n\n---Evaluation Choices---")
    text.insert(END, f"\n\tBetter Option : {"Compound" if com>sim else "Simple"}")
    text.insert(END, f"\n\tDifference: {max(com,sim)-min(com,sim)}")
frame = Frame(master=root)
guide = Label(text="P\tR\tT\t   ", font="Helvetica 10")
entry1 = Entry(master=frame, width=5)
entry2 = Entry(master=frame, width=5)
entry3 = Entry(master=frame, width=5)
button = Button(master=frame, text="Calculate", command=calc, font="Helvetica 10")
text = Text(height=13)



guide.pack()
entry3.pack(side=LEFT, ipady=3, padx=10)
entry2.pack(side=LEFT, ipady=3, padx=10)
entry1.pack(side=LEFT, ipady=3, padx=10)
button.pack()
frame.pack()
text.pack(pady=10)


root.mainloop()
messagebox.showinfo("Visit the app again", "Do not Quit - Interest Calculator - Used to calculate and compare Simple And Compound interest outcomes and analyse to the degree of 30 d.p.")