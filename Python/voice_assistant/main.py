import speech_recognition as sr
import pyttsx3
import commands
import sys


# initializators
rec = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 210)


# variables
voices = engine.getProperty('voices')
preferred_music_platform = 'youtube'
assistant_name = 'computer'
commands_filename = 'commands.txt'
commands_list = []
questions_list = []


# adds all the elements of commands.txt in commands_list
def LoadCommandList():
    with open(commands_filename) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]
        for line in lines:
            args = line.split('/')
            if args[0].__contains__('-'):
                continue
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


# finds in the commands.txt the equivalent method
def RunCommand(command):
    filename = ''

    for index, question in enumerate(questions_list):
        for word in command.split(' '):
            if word == question:
                filename = commands_list[index][1]
                break
            else:
                # no match
                Speak('Non credo di aver capito bene.')
                return

    # converts string to method and runs it
    method = getattr(commands, filename).Main('', command)
    filename = ''


def LoadQuestionsList():
    for doubles in range(len(commands_list)):
        for words in enumerate(commands_list[doubles]):
            for num in str(words[0]):
                if num == '0':
                    questions_list.append(words[int(num) - 1])
    



# main method - listening and running RunCommand(command)
def Listening():
    print('Ready to help you!')
    while True:
        with sr.Microphone() as mic:
            try:
                rec.adjust_for_ambient_noise(mic)
                voice = rec.listen(mic)
                command = str(rec.recognize_google(voice, language='it-IT')).lower()
                print('command: {}.'.format(command))
                if command.__contains__(assistant_name):
                    command = command.replace(assistant_name, '')
                    RunCommand(command)

            except sr.UnknownValueError:
                pass
            except KeyboardInterrupt:
                print('Interrupted manually')
                sys.exit(0)



if __name__ == "__main__":
    LoadCommandList()
    LoadQuestionsList()
    Listening()