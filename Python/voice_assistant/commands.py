import datetime
import pywhatkit
import spotipy
import webbrowser
import tekore as tk
from spotipy.oauth2 import SpotifyClientCredentials
import main

class SearchOnYt():
    def Main(self, command):
        if main.preferred_music_platform == 'youtube':
            command = command.replace('riproduci ', '')
            pywhatkit.playonyt(command)
        elif main.preferred_music_platform == 'spotify':
            # conf = ('4dabb5933c0d49058846c549c6a703ba', '2aaa36256ccb43b88523498815b2416d', 'https://open.spotify.com/track/0vlCOzte4bru0gK74lfUIJ?si=43f59139a7144465')
            # token = tk.prompt_for_user_token(*conf, scope=tk.scope.every)
            # spotify = tk.Spotify(token)
            # tracks = spotify.current_user_top_tracks(limit=1)
            # spotify.playback_start_tracks([t.id for t in tracks.items])


            # spotify = spotipy.Spotify(language='IT', auth='4dabb5933c0d49058846c549c6a703ba')
            # results = spotify.search(q=command.replace('riproduci ', ''), type='track', limit=1, market='IT')
            # link = results['tracks']['href']
            # webbrowser.open(link)
            
            main.Speak('Questa funzione non è ancora disponibile.')


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