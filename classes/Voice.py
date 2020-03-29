from subprocess import Popen
import pyttsx3, os

class Voice:  # Threaded text to speech command

    def __init__(self):
        
        self.engine = pyttsx3.init()  # Initialize text to speech library
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[1].id)

    def say(self, msg):
        dir_path = os.path.dirname(os.path.dirname( __file__ )) + '\\speak.py'  # Get relative path to speak.py depending on where script is executed
        Popen(["python", dir_path, msg])  # Run threaded background command


if (__name__ == "__main__"):
    voice = Voice()
    voice.say("""Hello, Kai, how is your day! 
    Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s
    """);
    while True:
        print("I'm threaded!")