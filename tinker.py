from Tkinter import *
import tkMessageBox
#from PIL import ImageTk, Image //can use this for imaging
import time


root = Tk()


def getInstructions():
	tkMessageBox.showinfo("Instructions", "***Insert Instructions Here***")

def calculateText():
	tkMessageBox.showinfo("Example", "Example doeeeee")

root.geometry("600x400")
root.title("Braille Keyboard")

#come back and work on importing the jpg file within labelframe
labelframe = LabelFrame(root, text="Welcome to the Braille Keyboard")
labelframe.pack(fill="both")

inside = Label(labelframe, text="This is an open, free text to speech braille keyboard", height=10, width=40)
inside.pack()

#make a button for instructions, add the command 'display functions'
instructions = Button(text="Instructions", command=getInstructions)
instructions.pack(side=TOP)

#make text area for entering data
userLabel = Label(root, text="Enter characters: ")
submit = Button(text="submit", command=calculateText)
submit.pack()
userLabel.pack()

userEntry = Entry(root, bd =5)
userEntry.pack()

#make an area for displaying the data
textOutput = Text(root)
textOutput.insert(INSERT, "hello")
textOutput.pack(side = RIGHT);



#footer = LabelFrame(root, text=" ")
#footer.pack(fill="both")
#toes = Label(footer, text="\n\n\n\n")
#toes.pack()
#var = StringVar();
#label = Message( root, textvariable=var, relief=RAISED, width=200 )

#var.set("Zachary Yee\nSeth Balodi\nColm Gallagher")
#label.pack()


root.mainloop()
