import tts
import os

valid = "sdfjkl"
alpha = {"100000":"a","110000":"b","100100":"c","100110":"d","100010":"e","110100":"f","110110":"g","110010":"h","010100":"i","010110":"j","101000":"k","111000":"l","101100":"m","101110":"n","101010":"o","111100":"p","111110":"q","111010":"r","011100":"s","011110":"t","101001":"u","111001":"v","010111":"w","101101":"x","101111":"y","101011":"z","001101":".","001000":",","001100":":","001101":"$","001011":"?","001110":"!"}
braille = {"a":u"\u2801","b":u"\u2803","c":u"\u2809","d":u"\u2819","e":u"\u2811","f":u"\u280b","g":u"\u281b","h":u"\u2813","i":u"\u280a","j":u"\u281a","k":u"\u2805","l":u"\u2807","m":u"\u280d","n":u"\u281d","o":u"\u2815","p":u"\u280f","q":u"\u281f","r":u"\u2817","s":u"\u280e","t":u"\u281e","u":u"\u2825","v":u"\u2827","w":u"\u283a","x":u"\u282d","y":u"\u283d","z":u"\u2835",".":u"\u2832",",":u"\u2802",":":u"\u2812","$":u"\u2832","?":u"\u2826","!":u"\u2816"}

alpha = {"*ooooo":"a","**oooo":"b","*oo*oo":"c","*oo**o":"d","*ooo*o":"e","**o*oo":"f","**o**o":"g","**oo*o":"h","o*o*oo":"i","o*o**o":"j","*o*ooo":"k","***ooo":"l","*o**oo":"m","*o***o":"n","*o*o*o":"o","****oo":"p","*****o":"q","***o*o":"r","o***oo":"s","o****o":"t","*o*oo*":"u","***oo*":"v","o*o***":"w","*o**o*":"x","*o****":"y","*o*o**":"z"}


def printKey(letter,keys):
    os.system('clear')
    print u"{0}:{1}".format(letter,braille[letter])

def printStr(str):
    os.system('clear')
    print str

class Braille:
    def __init__(self):
        self.output = ""
        self.word = ""

    def setKeys(self,keys):
        result = "oooooo"
        for key in keys:
            if(key.lower() in valid):
                val = valid.find(key.lower())
                result= result[:val]+"*"+result[val+1:]
        return result
    def toBraille(letter):
        return braille[letter]

    def write(self):
        keys = raw_input()
        # Backspace:
        if ";" in keys:
            for key in keys:
                if key == ";":
                    if(len(self.output) > 0):
                        self.output = self.output[:-1]
                        if(len(self.output) >= 0):
                            i=-1
                            word = ""
                            while(len(self.output) >= i*-1 and self.output[i] != " "):
                                word = self.output[i] + word
                                i-=1
                            self.word = word
            tts.say(word)
            printStr(word)
        # End of sentence:
        if keys == "":
            tts.say(self.output)
            printStr(self.output)
            return -1
        # Space:
        elif keys == " ":
            tts.say(self.word)
            printStr(self.word)
            self.output+=" "
            self.word = ""
            return 1
        # Letter:
        else:
            keysPressed = self.setKeys(keys)
            if alpha.has_key(keysPressed):                    
                letter = alpha[keysPressed]
                if "a" in keys.lower():
                    letter = letter.upper()
                tts.say(letter)
                printKey(letter,keysPressed)
                self.output += letter
                self.word += letter
                return 1
            else:
                return 1
    def __str__(self):
        return self.output

def writer():
    b = Braille()
    bw = 1
    while bw!=-1:
        bw = b.write()

writer()     

