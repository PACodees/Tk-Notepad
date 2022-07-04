from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Grocery List")
# test commit
def saveFile():
    userInput = userEntry.get()
    userFileName = fileName.get()
    f = open(f"{userFileName}.txt", "w")
    f.write(userInput)
    savedBox = messagebox.showinfo("File Saved Successfully", "File Saved Successfully")

def loadFile():
    userFileName = fileName.get()
    f = open(f"{userFileName}.txt", "r")
    fileText = f.read()
    userEntry.insert(0, fileText)
    f.close()

title = Label(root, text="Notepad", bg="gray", width=33)
title.grid(row=0, column=0, columnspan=3)

userEntry = Entry(root, width=33)
userEntry.grid(row=1, column=0, columnspan=3, pady=10)
userEntry.bind("<Return>", saveFile)

saveButton = Button(root, text="Save", bg="gray", command=saveFile)
saveButton.grid(row=2, column=0, pady=5)

fileName = Entry(root)
fileName.grid(row=2, column=1)
fileName.bind("<Return>", saveFile)

loadButton = Button(root, text="Load", bg="gray", command=loadFile)
loadButton.grid(row=2, column=2)

root.mainloop()