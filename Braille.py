valid = "sdfjkl"
alpha = {"100000":"a","110000":"b","100100":"c","100110":"d","100010":"e","110100":"f","110110":"g","110010":"h","010100":"i","010110":"j","101000":"k","111000":"l","101100":"m","101110":"n","101010":"o","111100":"p","111110":"q","111010":"r","011100":"s","011110":"t","101001":"u","111001":"v","010111":"w","101101":"x","101111":"y","101011":"z"}

class Braille:
    def __init__(self):
        self.output = ""
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
            return -1
        elif keys == " ":
            self.output+=" "
            return self.output
        else:
            temp = self.setKeys(keys)
            if alpha.has_key(temp):
                letter = alpha[temp]
                self.output += letter
                return self.output
            else:
                return self.output
    def __str__(self):
        return self.output
def writer(b):
    bw = b.write()
    while bw!=-1:
        print bw
        bw = b.write()

                    
                    
                


