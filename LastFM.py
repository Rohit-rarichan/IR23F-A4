# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645
import urllib,json
from OpenWeather import online_posting
from WebAPI import WebAPI


class LastFM(WebAPI):
    # API KEY = 0f3b7d4b1bcbf510a016140f60ee960d
    def __init__(self, music_apikey) -> None:
        self.apikey = music_apikey
        self.album_data = None 
        self.artist_tracks = None 
        self.chart_top = None
        self.chart_artists = None

    def load_data(self) -> None:
        ''' Calls the web api using the required values and stores the response in class data attributes.'''
        if self.apikey is None:
            raise ValueError("The API Key has not been set")
        try:
            method = input("What method would you like to implement")
            if method == "artist.gettoptracks":
                artist = input("Enter the name of a artist")
                url = f"http://ws.audioscrobbler.com/2.0/?method={method}&artist={artist}&api_key={self.apikey}&format=json"
                self.artist_tracks = super()._download_url(url)
                
                tracks = []
                for i in range(len(self.artist_tracks['toptracks']['track'])):
                    tracks.append(self.artist_tracks['toptracks']['track'][i]['name'])
                print(tracks)
                self.artist_tracks = tracks
            elif method == "chart.gettopartists":
                url = f"http://ws.audioscrobbler.com/2.0/?method={method}&api_key={self.apikey}&format=json"
                self.chart_top = super()._download_url(url)
                artists = []
                for i in range(len(self.chart_top['artists']['artist'])):
                    artists.append(self.chart_top['artists']['artist'][i]['name'])
                print(artists)
                self.chart_artists = artists
            elif method == "album.getinfo":
                artist = input("Enter the name of a artist")
                album = input("Enter the name of a album")
                url = f"http://ws.audioscrobbler.com/2.0/?method={method}&api_key={self.apikey}&artist={artist}&album={album}&format=json"
                self.album_data = super()._download_url(url)
                print(self.album_data)
        except urllib.error.URLError as e:
            raise ValueError(f"Failed to connect to OpenWeather API")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise ValueError("Requested remote API is unavailable")
            elif e.code == 503:
                raise ValueError("The API source listed is not currently working")
            else:
                raise ValueError("HTTP ERROR:", e.code)
            
    def transclude(self, message:str) -> str:
        '''  Replaces keywords in a message with associated API data.:param message: The message to transclude
  :returns: The transcluded message'''
        message_list = message.split(' ')
        keyword = [x for x in message_list if "@" in x]
        for i in keyword:
            if i == '@album_info':
                message = message.replace('@album_info', str(self.album_data))
            elif i == '@top_tracks':
                message = message.replace('@top_tracks', str(self.artist_tracks))
            elif i == '@chart_tops':
                message = message.replace('@chart_tops', str(self.chart_artists))
        return message


def FM_main() -> None:
    music_apikey = "3da7a1597218670366ed9c7f959dccde"
    open_music = LastFM(music_apikey)
    open_music.set_apikey(music_apikey)
    open_music.load_data()
    message = input("Enter your message with the keyword")
    message = open_music.transclude(message)
    online_posting(message)



        

