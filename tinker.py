from Tkinter import *
import Tkinter as tk
import tkMessageBox
#from PIL import ImageTk, Image //can use this for imaging
import Braille as br


root = Tk()
b = br.Braille()


def getInstructions():
	tkMessageBox.showinfo("Instructions", "This Braille Board program converts a regular keyboard into a braille keyboard. The format is that of the Perkins Brailler, a well known and utilized brailler. This program works as follows: The user recognizes six internal keys that map to one of hte 6 dots of the familiar braille notation. The user must find the tactile bumps over the 'F' and 'J' keys. The user's thumb will then rest on the spacebar. This position will allow for the user to input from all the valid keys: a, s, d, f, j, k, l, ; and <spacebar>. For full instructions of how to run the program, read the README.md on github.com/mecolmg/BrailleBoard/blob/master/README.md")

def toClipboard():
	root.clipboard_clear()
	root.clipboard_append(b.output)

root.geometry("1000x800")
root.title("Braille Keyboard")

#come back and work on importing the jpg file within labelframe
labelframe = LabelFrame(root, text="Welcome to the Braille Keyboard")
labelframe.pack(fill="both")

inside = Label(labelframe, text="This is an open, free text to speech braille keyboard")
inside.pack(fill=X)

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
