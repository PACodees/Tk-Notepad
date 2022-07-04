from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Grocery List")
def saveFile(text):
    userInput = userEntry.get()
    userFileName = fileName.get()
    f = open(f"{userFileName}.txt", "w")
    f.write(userInput)
    savedBox = messagebox.showinfo("File Saved Successfully", "File Saved Successfully")

def loadFile():
    userFileName = fileName.get()
    if len(userFileName) != 0:
        f = open(f"{userFileName}.txt", "r")
        fileText = f.read()
        userEntry.insert(0, fileText)
        f.close()
    else:
        errorBox = messagebox.showerror("Error loading", "Please enter a file name to load.")

title = Label(root, text="Notepad", bg="gray", width=70, font="Arial 30")
title.grid(row=0, column=0, columnspan=3)

userEntry = Entry(root, width=40, font="Arial 20")
userEntry.grid(row=1, column=0, columnspan=3, pady=20)
userEntry.bind("<Return>", saveFile)

saveButton = Button(root, text="Save", bg="gray", command=saveFile, width=15, height=3, font="Arial 10")
saveButton.grid(row=2, column=0, pady=10)

fileName = Entry(root, font="Arial 15")
fileName.grid(row=2, column=1)
fileName.bind("<Return>", saveFile)

loadButton = Button(root, text="Load", bg="gray", command=loadFile, width=15, height=3, font="Arial 10")
loadButton.grid(row=2, column=2)
# testing commit
root.mainloop()