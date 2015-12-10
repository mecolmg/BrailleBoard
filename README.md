# Braille Board
#####Created by: Colm Gallagher, Zachary Yee, Seth Balodi
### Introduction:
Braille Board is a program that converts a regular keyboard into a braille keyboard for the blind. The format mimics that of the keyboard shown below, known as the **Perkins Brailler**:

![Image of Braille Keyboard](https://images.indiegogo.com/file_attachments/309591/files/20140115014447-BrailleKeyboard.jpg?1389779087)

The brailler is a very simple concept, the six internal keys each map to one of the 6 dots of the familiar braille notation. These keyboards are very expensive to purchase, but are at the same time very usefull for blind children, who may not be familiar with the locations of letters on a standard keyboard.

### Features:
* Braille input without expensive keyboard
* Text-To-Speach Features
* Copy to clipboard functionality
* Most common characters
* GUI

### Implementation:
With our implementation, the children just have to find the two tactile bumps over the 'F' and 'J' keys, and are able to keep their hands there, with their thumbs resting on the space. The mappings for keys are as follows:

![Image of Braille Alphabet](http://faculty.washington.edu/chudler/gif/braille.gif)

Limited punctutation is also included:

| Character | Braille  |
| --------- | -------  |
| .         | &#x2832; |
| ,         | &#x2802; |
| :         | &#x2812; |
| ?         | &#x2826; |
| !         | &#x2816; |

The key mappings are as follows:

Key | Mapping
----| -------
a | New Line
s | 3
d | 2
f | 1
j | 4
k | 5
l | 6
; | Backspace

Which follows this pattern:

![Pattern](http://www.faculty.umb.edu/wendy_buckley/BrailleI/class01/images/image001.jpg)

### Needed Libraries:
Additional libraries used include:
* [eSpeak](http://espeak.sourceforge.net/)
* [Tkinter](https://wiki.python.org/moin/TkInter)

### Running the program:
To run the program, execute 'tinker.py' from the terminal using the command 'python tinker.py'.
You will be displayed with a display like this:

![Project](http://i.imgur.com/9xJNlia.png)

You can begin typing in letters, hitting the space bar after each letter to signify the end of those letters. Each letter will be spoken out loud to ensure the user knows what he or she is typing. Hitting the space bar with no other letters will result in a space being typed and the last word written being pronounced. 

### Other remarks:
This project has only been tested on linux and is not guarunteed to work on other systems. An implementation into the OS could not be reached without using software used in common keyloggers, and was therefore set aside to be pursued later. 
