import speech_recognition as sr
import pyttsx3


def change_voice(engine, index=0):
    engine.setProperty('voice', voices[index].id)
    return True


# initializators
rec = sr.Recognizer()
engine = pyttsx3.init()

# variables
current_voice = engine.getProperty('voice')
voices = engine.getProperty('voices')
change_voice(engine, 0) #sets language to italian



# prints avaible languages in the os
index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1


def Speak(text):
    engine.say(text)
    engine.runAndWait()



while True:
    with sr.Microphone() as mic:
        print('listening')
        voice = rec.listen(mic)
        command = rec.recognize_google(voice)


Speak("ciao, sono italiano e mi piace molto la pasta col sugo. Viva la mafia e il duce!!!")