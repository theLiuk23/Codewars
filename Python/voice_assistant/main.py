import urllib.request
import re
import webbrowser
import speech_recognition as sr
import pyttsx3
import sys
import webbrowser
import pywhatkit



# initializators
rec = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# variables
voices = engine.getProperty('voices')
assistant_name = ''
commands_filename = 'commands.txt'
commands_list = []


class SearchOnYt():
    def Main(self, command):
        command = command.replace('mozart', 'banane')
        print("ARG: " + command)
        pywhatkit.playonyt(command)


with open(commands_filename) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        args = line.split('/')
        commands_list.append([args[0], args[1]])


# prints avaible languages in the os
# index = 0
# for voice in voices:
#    print(f'index-> {index} -- {voice.name}')
#    index +=1


def Speak(text):
    engine.say(text)
    engine.runAndWait()
    return True


def RunCommand(command):
    filename = ''
    for index, result in enumerate(commands_list):
        if result.__contains__(command):
            filename = commands_list[index][1]
            break
    SearchOnYt().Main(command)



def Listening():
    while True:
        with sr.Microphone() as mic:
            print('listening')
            voice = rec.listen(mic)
            command = rec.recognize_google(voice, language='it-IT').lower()
            print('command: {}'.format(command))
            if command.__contains__(assistant_name):
                RunCommand(command.replace(assistant_name + " ", ''))




if __name__ == "__main__":
    Listening()