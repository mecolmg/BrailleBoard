from espeak import espeak

def say(word):
    espeak.synth(word)