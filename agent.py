from classes.Listener import Listener
from classes.Voice import Voice

# Objects for listener and voice
listener = Listener()
voice = Voice()

listener.run()  # Run the threaded listener

prev_status = ""

while True:
    curr_status = listener.get_status()

    if (curr_status is not prev_status):
        voice.say(curr_status)

    print("Command:", listener.get_command())
    print("Status:", listener.get_status())
    prev_status = curr_status
    
