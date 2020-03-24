import pyttsx3

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize text to speech library

    def say(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()
