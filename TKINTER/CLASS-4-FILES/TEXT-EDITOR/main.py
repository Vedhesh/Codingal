from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window = Tk()
window.title("Notepad--")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    openpath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])

    if not openpath:
        return
    
    editor.delete(1.0, END)

    with open(openpath, "r") as inputfile:
        text = inputfile.read()
        editor.insert(END, text)
        inputfile.close()

    window.title(f"Notepad-- *{openpath}")

def save_file():
    savepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not savepath:
        return
    with open(savepath, "w") as outputfile:
        text = editor.get(1.0, END)
        outputfile.write(text)
    window.title(f"Notepad-- *{savepath}")

editor = Text(window)
btnframe = Frame(window, relief=RIDGE, bd=2)
openbtn = Button(btnframe, text="Open File", command=open_file)
savebtn = Button(btnframe, text="Save As", command=save_file)
openbtn.grid(row=0, column=0, sticky=EW, padx=5, pady=5)
savebtn.grid(row=1, column=0, sticky=EW, padx=5)
btnframe.grid(row=0, column=0, sticky=NS)
editor.grid(row=0, column=1, sticky=NSEW)
window.mainloop()


