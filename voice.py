import pyttsx3
import speech_recognition as sr

class Voice:
    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()

class Listener:

    name = "Alexa"
    command = ""

    def __init__(self):
        self.r = sr.Recognizer()

    def listen_for_command(self):
        with sr.Microphone() as source:     # mention source it will be either Microphone or audio files.
            print("Speak Anything :")
            while True:
                audio = self.r.listen(source)        # listen to the source
                try:
                    text = self.r.recognize_google(audio)    # use recognizer to convert our audio into text part.
                    if self.name.lower() in text.lower():
                        fullmsg = text
                        self.command = text.lower().split(self.name.lower())[1].strip()
                        return command
                except:
                    print("Sorry could not recognize your voice")    # In case of voice not recognized 
        return ""
        
Listener = Listener()
print(Listener.listen_for_command())
#voice = Voice()

#voice.say("Hello, kai")

