import pyttsx3
import threading

class Voice:
    def __init__(self):
        
        self.engine = pyttsx3.init()  # Initialize text to speech library
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def __say(self, msg):
        self.engine.say(msg)
        self.engine.runAndWait()
        self.engine.stop()

    def say(self, msg):
        t1 = threading.Thread(target=self.__say(msg))
        t1.daemon = True
        t1.start()
        
        
if (__name__ == "__main__"):
    voice = Voice()
    voice.say("""Hello, Kai, how is your day! 
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
    """);
    while True:
        print("hi")
    
