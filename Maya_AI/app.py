from maya_listen import listen
from maya_voice import speak
from maya_brain import think

speak("Hello Mayank, I am Maya. How can I help you?")

while True:

    command = listen()

    if command == "":
        continue

    if "stop" in command.lower():
        speak("Goodbye Mayank")
        break

    response = think(command)
    speak(response)