import pyttsx3
import speech_recognition as sr

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()

class Listener:

    def __init__(self):
        self.r = sr.Recognizer()

voice = Voice()

voice.say("Hello, kai")

r = sr.Recognizer()

with sr.Microphone() as source:
    # read the audio data from the default microphone
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    print(text)