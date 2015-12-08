from espeak import espeak

def say(word):
    for c in word:  #says one letter at a time
        espeak.synth(c)
