import tts

valid = "sdfjkl"
alpha = {"100000":"a","110000":"b","100100":"c","100110":"d","100010":"e","110100":"f","110110":"g","110010":"h","010100":"i","010110":"j","101000":"k","111000":"l","101100":"m","101110":"n","101010":"o","111100":"p","111110":"q","111010":"r","011100":"s","011110":"t","101001":"u","111001":"v","010111":"w","101101":"x","101111":"y","101011":"z"}

class Braille:
    def __init__(self):
        self.output = ""
        self.word = ""

    def setKeys(self,keys):
        result = "000000"
        for key in keys:
            if(key in valid):
                val = valid.find(key)
                result= result[:val]+str(1)+result[val+1:]
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


