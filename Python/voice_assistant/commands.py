import threading
import speech_recognition as sr
from spotipy.oauth2 import SpotifyClientCredentials
from pygooglenews import GoogleNews
from pathlib import Path
import time
import playsound
import webbrowser
import datetime
import pywhatkit
import spotipy
import re
import sys
import main

music_platform = 'youtube'
# TODO: music_platform in txt file

class SearchMusic(object):
    def Main(self, command):
        command = command.replace('riproduci ', '')
        if music_platform == 'youtube':
            pywhatkit.playonyt(command)
        elif music_platform == 'spotify':
            client_id = '4dabb5933c0d49058846c549c6a703ba'
            client_secret = '2aaa36256ccb43b88523498815b2416d'
            spotifyObject = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
            searchResults = spotifyObject.search(command, 1, 0, 'track')
            link = searchResults['tracks']['items'][0]['external_urls']['spotify']
            webbrowser.open(link, 0)


class Answers(object):
    def Main(self, command):
        if command.__contains__('ciao'):
            main.Speak(f'Ciao, sono {main.assistant_name}, come posso aiutarti?')
        elif command.__contains__('come stai') or command.__contains__('bene'):
            main.Speak('Sono carico, fino a quando non mi spegni.')
        elif command.__contains__('ore'):
            hour = str(datetime.datetime.now().hour)
            minute = str(datetime.datetime.now().minute)
            main.Speak(f'Sono esattamente le {hour} e {minute}.')
        elif command.__contains__('v*********') or command.__contains__('inculo'):
            main.Speak(f'Vacci tu brutto stronzo di merda!')


class ChangeMusicPlatform(object):
    def Main(self, command):
        if command.__contains__('youtube'):
            music_platform = 'youtube'
        elif command.__contains__('spotify'):
            music_platform = 'spotify'

        main.Speak(f'Ho cambiato la piattaforma musicale predefinita in {music_platform}.')

    
    def change_txt(self, platform):
        with open('settings.txt') as settings:
            lines = settings.readlines()
            for line in lines:
                if line.__contains__('music_platform'):
                    mp_line_index = lines.index('music_platform')
                    break
            settings.close()

        with open('settings.txt', 'w') as settings:
            # settings.
            settings.close()


class ReadNews(object):
    fonte = 'Google News'

    def get_num(self, command):
        numbers = {'prima':1, 'uno':1, 'un': 1, 'due': 2, 'tre':3, 'quattro':4, 'cinque':5, 'sei':6, 'sette':7, 'otto':8, 'nove':9, 'dieci':10}
        for word in command.split(' '):
            if numbers.__contains__(word):
                return numbers[word]

        try:
            return int(re.search(r'\d+', command).group())
        except:
            return 5


    def Main(self, command):
        num = self.get_num(command)
        index = 1

        if num == 1:
            main.Speak(f'Ecco la prima notizia da {self.fonte}')
        else:
            main.Speak(f'Ecco le prime {num} notizie da {self.fonte}')
            
        gn = GoogleNews(lang='it', country='IT')
        top = gn.top_news()

        for item in top['entries'][:num]:
            title = item['title'].split('-')[0] #removes the source from the end of the string
            main.Speak(f'{index}, {title}')
            index = index + 1


class SetTask(object):
    orario = [18, 40]
    memo = None
    timer = None

    def ask_date(self, attempts):
        rec = sr.Recognizer()
        week_days = {'lunedì':0, 'martedì':1, 'mercoledì':2, 'giovedì':3, 'venerdì':4, 'sabato':5, 'domenica':6}
        if attempts == 0:
            main.Speak('Certo. Che giorno?')
        if attempts == 3:
            return
        with sr.Microphone() as mic:
            try:
                rec.adjust_for_ambient_noise(mic)
                voice = rec.listen(mic)
                day = str(rec.recognize_google(voice, language='it-IT')).lower()
                if week_days.__contains__(day.lower()):
                    return week_days[day.lower()]
                else:
                    raise Exception('No day provided.')
            except:
                main.Speak('Non ho capito che giorno. Ripeti per favore')
                self.ask_date(attempts + 1)

    def ask_time(self, attempts):
        rec = sr.Recognizer()
        if attempts == 0:
            main.Speak('Ok, a che ora?')
        if attempts == 3:
            return
        with sr.Microphone() as mic:
            try:
                rec.adjust_for_ambient_noise(mic)
                voice = rec.listen(mic)
                time = str(rec.recognize_google(voice, language='it-IT')).lower()
                print(f'PURE TIME: {time}')
                if time.__contains__(':'):
                    time_list = time.split(':')
                    if int(re.search(r'\d+', time_list[0]).group()) < 24:
                        self.orario = [int(re.search(r'\d+', time_list[0]).group()), int(time_list[1])]
                        print(f'TIME: {self.orario}')
                    else: raise Exception('Hour greater than 23')
                elif int(re.search(r'\d+', time).group()) < 24:
                    self.orario = time
                else:
                    raise Exception('No number provided')
            except Exception as e:
                print(e)
                main.Speak('Non ho capito a che ora. Ripeti per favore')
                self.ask_time(attempts + 1)

    def set_task(self, day):
        today = datetime.datetime.today().weekday()
        remaining_days = day - today
        time = self.orario
        todays_minutes = int(datetime.datetime.now().hour * 60 + datetime.datetime.now().minute)
        self.timer = time[0] * 60 + int(time[1]) + 1440 * int(remaining_days) - todays_minutes
        if self.timer <= 0:
            raise Exception('The task date must be within a week of time.')
        main.Speak(f'Bene! Il timer si attiverà tra {self.timer} minuti')
        thread = threading.Thread(target=self.start_timer)
        thread.start()

    def start_timer(self):
        time.sleep(int(self.timer) * 60)
        main.Speak(f'Hey, ricordati di {self.memo}. Mi raccomando!')
        sound_file_location = Path(__file__).parent + '/DieForYou.mp3'
        print(f'SOUND PATH: {sound_file_location}')
        playsound.playsound(sound_file_location)
        # sound doesn't work (?)

    def Main(self, command):
        self.memo = command.split('di ')[1]
        day = self.ask_date(0)
        self.ask_time(0)
        self.set_task(day)


class Stop(object):
    def Main(self, command):
        print(f'Closing the istance of the script')
        sys.exit(0)