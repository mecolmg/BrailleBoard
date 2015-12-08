import tts

valid = "sdfjkl"
alpha = {"*ooooo":"a","**oooo":"b","*oo*oo":"c","*oo**o":"d","*ooo*o":"e","**o*oo":"f","**o**o":"g","**oo*o":"h","o*o*oo":"i","o*o**o":"j","*o*ooo":"k","***ooo":"l","*o**oo":"m","*o***o":"n","*o*o*o":"o","****oo":"p","*****o":"q","***o*o":"r","o***oo":"s","o****o":"t","*o*oo*":"u","***oo*":"v","o*o***":"w","*o**o*":"x","*o****":"y","*o*o**":"z"}


def printKey(letter,keys):
    print "%s:\t%c%c\n\t%c%c\n\t%c%c" % (letter,keys[0],keys[3],keys[1],keys[4],keys[2],keys[5])

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

    def write(self):
        keys = raw_input()
        if keys == "":
            tts.say(self.output)
            return -1
        elif keys == " ":
            tts.say(self.word)
            self.output+=" "
            self.word = ""
            return 1
        else:
            keysPressed = self.setKeys(keys)
            if alpha.has_key(keysPressed):
                letter = alpha[keysPressed]
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

