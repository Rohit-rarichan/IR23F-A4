# lastfm.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645
import urllib,json
from OpenWeather import _download_url



class LastFM:
    # API KEY = 0f3b7d4b1bcbf510a016140f60ee960d
    def __init__(self, music_apikey) -> None:
        self.apikey = music_apikey
        self.album_data = None 
        self.artist_tracks = None 
        self.chart_top = None
        self.chart_artists = None

    def set_apikey(self, apikey:str) -> None:
        '''Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service
        '''
        self.apikey = apikey
    def load_data(self) -> None:
        ''' Calls the web api using the required values and stores the response in class data attributes.'''
        if self.apikey is None:
            raise ValueError("The API Key has not been set")
        try:
            method = input("What method would you like to implement")
            if method == "artist.gettoptracks":
                artist = input("Enter the name of a artist")
                url = f"http://ws.audioscrobbler.com/2.0/?method={method}&artist={artist}&api_key={self.apikey}&format=json"
                self.artist_tracks = _download_url(url)
                
                tracks = []
                for i in range(len(self.artist_tracks['toptracks']['track'])):
                    tracks.append(self.artist_tracks['toptracks']['track'][i]['name'])
                print(tracks)
                self.artist_tracks = tracks
            elif method == "chart.gettopartists":
                url = f"http://ws.audioscrobbler.com/2.0/?method={method}&api_key={self.apikey}&format=json"
                self.chart_top = _download_url(url)
                artists = []
                for i in range(len(self.chart_top['artists']['artist'])):
                    artists.append(self.chart_top['artists']['artist'][i]['name'])
                print(artists)
                self.chart_artists = artists
            elif method == "album.getinfo":
                artist = input("Enter the name of a artist")
                album = input("Enter the name of a album")
                url = f"http://ws.audioscrobbler.com/2.0/?method={method}&api_key={self.apikey}&artist={artist}&album={album}&format=json"
                self.album_data = _download_url(url)
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



def FM_main() -> None:
    music_apikey = "3da7a1597218670366ed9c7f959dccde"
    open_music = LastFM(music_apikey)
    open_music.set_apikey(music_apikey)
    open_music.load_data()

        

