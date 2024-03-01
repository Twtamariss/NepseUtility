import pyttsx3
def play(message, rate = 110, volume = 3):
    engine = pyttsx3.init()
    engine.setProperty('rate',rate)
    engine.setProperty('volume', volume)
    engine.say(message)
    engine.runAndWait()
