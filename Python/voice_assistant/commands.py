from spotipy.oauth2 import SpotifyClientCredentials
import webbrowser
import datetime
import pywhatkit
import spotipy
import main


class SearchMusic():
    def Main(self, command):
        command = command.replace('riproduci ', '')
        if main.preferred_music_platform == 'youtube':
            pywhatkit.playonyt(command)
        elif main.preferred_music_platform == 'spotify':
            client_id = '4dabb5933c0d49058846c549c6a703ba'
            client_secret = '2aaa36256ccb43b88523498815b2416d'
            spotifyObject = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))
            searchResults = spotifyObject.search(command, 1, 0, 'track')
            link = searchResults['tracks']['items'][0]['external_urls']['spotify']
            webbrowser.open(link)
            # TODO: play it automatically


class Answers():
    def Main(self, command):
        if command.__contains__('ciao'):
            main.Speak('Ciao, sono {}, come posso aiutarti?'.format(main.assistant_name))
        elif command.__contains__('come stai') or command.__contains__('bene'):
            main.Speak('Sono carico, fino a quando non mi spegni.')
        elif command.__contains__('ore'):
            hour = str(datetime.datetime.now().hour)
            minute = str(datetime.datetime.now().minute)
            main.Speak('Sono esattamente le {} e {}.'.format(hour, minute))


class ChangeMusicPlatform():
    def Main(slef, command):
        if command.__contains__('youtube'):
            main.preferred_music_platform = 'youtube'
        elif command.__contains__('spotify'):
            main.preferred_music_platform = 'spotify'
        main.Speak('Ho cambiato la piattaforma musicale predefinita in {}.'.format(main.preferred_music_platform))