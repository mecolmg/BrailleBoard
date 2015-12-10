from Tkinter import *
import Tkinter as tk
import tkMessageBox
#from PIL import ImageTk, Image //can use this for imaging
import Braille as br


root = Tk()
b = br.Braille()


def getInstructions():
	tkMessageBox.showinfo("Instructions", "***Insert Instructions Here***")

def calculateText():
	tkMessageBox.showinfo("Example", "Example doeeeee")

def toClipboard():
	root.clipboard_clear()
	root.clipboard_append(b.output)

root.geometry("1000x800")
root.title("Braille Keyboard")

#come back and work on importing the jpg file within labelframe
labelframe = LabelFrame(root, text="Welcome to the Braille Keyboard")
labelframe.pack(fill="both")

inside = Label(labelframe, text="This is an open, free text to speech braille keyboard", height=10, width=40)
inside.pack()

#make a button for instructions, add the command 'display functions'
instructions = Button(text="Instructions", command=getInstructions)
instructions.pack(side=TOP)

#make a button to copy to clipboard
clip = Button(text="Copy To Clipboard", command=toClipboard)
clip.pack(side=TOP)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)


#make text area for entering data
text = Text(root, state="disabled", font="Helvetica 16 bold")
text.pack(fill=tk.X)
text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text.yview)

keys = ""
def keydown(event):
	global keys
	if event.char == " ":
		if keys == "":
			keys = " "
		b.write(keys)
		text.config(state="normal")
		text.delete(1.0,END)
		text.insert(INSERT,b.output+"\n"+b.braille)
		text.config(state="disabled")
		keys = ""
	else:
		keys += event.char

root.bind("<KeyPress>", keydown)

root.mainloop()
