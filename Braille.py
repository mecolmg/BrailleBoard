import tts
import os

valid = "fdsjkl"
alpha = {"100000":"a","110000":"b","100100":"c","100110":"d","100010":"e","110100":"f","110110":"g","110010":"h","010100":"i","010110":"j","101000":"k","111000":"l","101100":"m","101110":"n","101010":"o","111100":"p","111110":"q","111010":"r","011100":"s","011110":"t","101001":"u","111001":"v","010111":"w","101101":"x","101111":"y","101011":"z","010011":".","010000":",","010010":":","011001":"?","011010":"!"}
braille = {"\n":"\n"," ":" ","a":u"\u2801","b":u"\u2803","c":u"\u2809","d":u"\u2819","e":u"\u2811","f":u"\u280b","g":u"\u281b","h":u"\u2813","i":u"\u280a","j":u"\u281a","k":u"\u2805","l":u"\u2807","m":u"\u280d","n":u"\u281d","o":u"\u2815","p":u"\u280f","q":u"\u281f","r":u"\u2817","s":u"\u280e","t":u"\u281e","u":u"\u2825","v":u"\u2827","w":u"\u283a","x":u"\u282d","y":u"\u283d","z":u"\u2835",".":u"\u2832",",":u"\u2802",":":u"\u2812","?":u"\u2826","!":u"\u2816"}

def printKey(letter,keys):
    os.system('clear')
    print u"{0}:{1}".format(letter,braille[letter.lower()])

def printStr(str):
    os.system('clear')
    print str

class Braille:
    def __init__(self):
        self.output = ""
        self.braille = ""
        self.word = ""

    def setKeys(self,keys):
        result = "000000"
        for key in keys:
            if(key.lower() in valid):
                val = valid.find(key.lower())
                result= result[:val]+"1"+result[val+1:]
        return result

    def toBraille(letter):
        return braille[letter]

    def write(self, keys):
        # keys = raw_input()

        # End of sentence:
        if keys == "":
            tts.say(self.output)
            printStr(self.output+"\n"+self.braille)
            return -1

        # Space:
        elif keys == " ":
            tts.say(self.word)
            printStr(self.output + "\n" + self.braille)
            self.output += " "
            self.braille += " "
            self.word = ""
            return 1

        # Backspace:
        elif ";" in keys:
            for key in keys:
                if key == ";":
                    if(len(self.output) > 0):
                        self.output = self.output[:-1]
                        self.braille = self.braille[:-1]
                        if(len(self.output) >= 0):
                            i=-1
                            word = ""
                            while(len(self.output) >= i*-1 and self.output[i] != " "):
                                word = self.output[i] + word
                                i-=1
                            self.word = word
            tts.say(self.word)
            printStr(self.output+"\n"+self.braille)
            return 1

        # Line space:
        elif keys == "a":
            self.output += "\n"
            self.word = ""
            self.braille += "\n"
            return 1

        # Uppercase:
        elif keys == "l":
            self.braille += u"\u2820"
            return 1

        # Letter:
        else:
            keysPressed = self.setKeys(keys)
            if alpha.has_key(keysPressed):                    
                letter = alpha[keysPressed]
                if len(self.braille) > 0 and self.braille[-1] == u"\u2820":
                    if letter.isalpha():
                        letter = letter.upper()
                    else:
                        self.braille = self.braille[:-1]
                tts.say(letter)
                printKey(letter,keysPressed)
                self.output += letter
                self.braille += braille[letter.lower()]
                self.word += letter
                return 1
            else:
                return 1
    def __str__(self):
        return self.output

# def writer():
#     b = Braille()
#     bw = 1
#     while bw!=-1:
#         bw = b.write()

# writer()     

