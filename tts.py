import pyttsx as tts

client = tts.init()

def say(word):
    client.say(word)
    client.runAndWait()
