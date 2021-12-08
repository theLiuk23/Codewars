import os
import speech_recognition as sr
import pyttsx3


def change_voice(engine, language='english', gender='VoiceGenderFemale'):
    for voice in engine.getProperty('voices'):
        if language in voice.languages:
            engine.setProperty('voice', voice.id)
            return True
    raise RuntimeError("Language '{}' for gender '{}' not found".format(language, gender))


rec = sr.Recognizer()
engine = pyttsx3.init()
current_voice = engine.getProperty('voice')
voices = engine.getProperty('voices')
# change_voice(engine, "\x05it", 'VoiceGenderMale')
engine.setProperty('voice', voices[41].id)


# voices = engine.getProperty('voices')
# for voice in voices:
#     print("Voice: %s" % voice.name)
#     print(" - ID: %s" % voice.id)
#     print(" - Languages: %s" % voice.languages)
#     print(" - Gender: %s" % voice.gender)
#     print(" - Age: %s" % voice.age)
#     print("\n")

# for voice in voices:
#     print(voice)
#     if voice.name == 'italian':
#         engine.setProperty('voice', voice.id)
#     else:
#         print("nessun italiano. sadge")

index = 0
for voice in voices:
   print(f'index-> {index} -- {voice.name}')
   index +=1


def Speak(text):
    engine.say(text)
    engine.runAndWait()



# while True:
#     with sr.Microphone() as mic:
#         mic.


Speak("ciao, sono italiano e mi piace molto la pasta col sugo. Viva la mafia e il duce!!!")