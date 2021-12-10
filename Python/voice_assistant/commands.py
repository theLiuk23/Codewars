import datetime
import pywhatkit
import main

class SearchOnYt():
    def Main(self, command):
        if main.preferred_music_platform == 'youtube':
            command = command.replace('riproduci ', '')
            pywhatkit.playonyt(command)
        elif main.preferred_music_platform == 'spotify':
            # TODO: implementation with spotify
            main.Speak('This function is not ready yet')


class Answers():
    def Main(self, command):
        if command.__contains__('ciao'):
            main.Speak('Ciao, sono {}, come posso aiutarti?'.format(main.assistant_name))
        elif command.__contains__('ore'):
            hour = str(datetime.datetime.now().hour)
            minute = str(datetime.datetime.now().minute)
            main.Speak('Sono esattamente le {} e {}'.format(hour, minute))


class ChangeMusicPlatform():
    def Main(slef, command):
        if command.__contains__('youtube'):
            main.preferred_music_platform = 'youtube'
        elif command.__contains__('spotify'):
            main.preferred_music_platform = 'spotify'
        main.Speak('Ho cambiato la piattaforma musicale predefinita in {}.'.format(main.preferred_music_platform))