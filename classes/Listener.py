import speech_recognition as sr

class Listener:
    
    name = "Alexa"
    status = ""
    command = ""

    def __init__(self):
        self.r = sr.Recognizer()
    
    def __detect_voice(self, audio):
        try:
            text = self.r.recognize_google(audio)
            print(text)
            if  (self.name.lower() in text.lower()):
                command = text.lower().split(self.name.lower())[1].strip()
                self.status = "succesful command"
                return command
            else:
                self.status = "sound detected, no keyword"
        except sr.UnknownValueError:
            self.status = "unknown sound"
        except sr.RequestError as e:
            self.status = "unable to read microphone"

        return ""

    def run_listener(self):
        with sr.Microphone() as source: 
            while True:                                                                      
                print("Speak:")                                                                                   
                audio = self.r.listen(source)   
                self.command = self.__detect_voice(audio)
                
    def get_command(self):
        return self.command

    def get_status(self):
        return self.status