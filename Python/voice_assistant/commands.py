from urllib.parse import urlencode
import datetime
import pywhatkit
import requests
import main
import base64


class SearchMusic():
    def Main(self, command):
        command = command.replace('riproduci ', '')
        if main.preferred_music_platform == 'youtube':
            pywhatkit.playonyt(command)
        elif main.preferred_music_platform == 'spotify':
            # see this awesome yt video --> https://youtu.be/xdq6Gz33khQ (58 minuti)
            client_id = '4dabb5933c0d49058846c549c6a703ba'
            client_secret = '2aaa36256ccb43b88523498815b2416d'
            spotify = SpotifyAPI(client_id, client_secret)
            spotify.perform_auth()
            search = spotify.search(command)
            print(search)


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'
    
    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_id == None:
            raise Exception('You must set both client id and client secret')
        client_creds = f'{client_id}:{client_secret}'
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            'Authorization': f'Basic {client_creds_b64}'
        }

    def get_token_data(self):
        return {
            'grant_type': 'client_credentials'
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        valid_request = r.status_code not in range(200, 299)
        if valid_request:
            raise Exception('Could not authenticate the client.')
        data = r.json()
        now = datetime.datetime.now()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    def get_access_token(self):
        auth_done = self.perform_auth()
        if not auth_done:
            raise Exception('Authentication failed')
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now or token is None:
            self.perform_auth()
            return self.get_access_token()
        return token

    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {'Authorization':f'Bearer {access_token}'}
        return headers

    def get_resource(self, lookup_id, resource_type='albums', version='v1'):
        endpoint = f'https://api.spotify.com/{version}/{resource_type}/{lookup_id}'
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def get_album(self, _id):
        return self.get_resource(_id, resource_type='albums')
    
    def get_artist(self, _id):
        return self.get_resource(_id, resource_type='artists')

    def search(self, query, search_type='track'):
        headers = self.get_resource_header()
        endpoint = 'https://api.spotify.com/v1/search'
        data = urlencode({'q': query, 'type':search_type.lower()})
        lookup_url = f'{endpoint}?{data}'
        r = requests.get(lookup_url, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()


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