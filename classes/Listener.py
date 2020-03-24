import speech_recognition as sr
import threading

class Listener:
    
    name = "Alexa"  # The name to trigger the listening
    status = ""  # The current status of the listener
    command = ""  # The command sentence of the text

    def __init__(self):
        self.r = sr.Recognizer()  # Create an object for the speech_recognition
    
    def __detect_voice(self, audio):
        '''
        Recognize audio stream and fetch command from text
        '''
        try:
            text = self.r.recognize_google(audio)  # Use google recognizer to get text
            if  (self.name.lower() in text.lower()):  # Check if keyword is in raw text
                command = text.lower().split(self.name.lower())[1].strip()
                self.status = "succesful command"
                return command
            else:
                self.status = "sound detected, no keyword"
        except sr.UnknownValueError:
            self.status = "unknown sound"
        except sr.RequestError:
            self.status = "unable to read microphone"

        return ""

    def __run_listener(self):
        '''
        Loop the continue listening for key word to trigger
        '''
        with sr.Microphone() as source: 
            while True:                                                                                
                audio = self.r.listen(source)   
                self.command = self.__detect_voice(audio)

    def run(self):
        '''
        Surface-level run function to start listener in threaded loop
        '''
        t1 = threading.Thread(target=self.__run_listener)
        t1.daemon = True
        t1.start()

    def get_command(self):
        '''
        Return the current command
        '''
        return self.command

    def get_status(self):
        '''
        Return the status of the listener
        '''
        return self.status

if __name__ == '__main__':
    listener = Listener()
    listener.run()
    while True:
        print("Command:", listener.get_command())
        print("Status:", listener.get_status())