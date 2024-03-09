# openweather.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645
# API KEY - 65518d2062b2ced79bbb83249bd10638
import urllib, json
from urllib import request,error

class OpenWeather:

    def __init__(self, zipcode, ccode) -> None:
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = None
    
    def set_apikey(self, apikey:str) -> None:
        ''' Sets the apikey required to make requests to a web API.:param apikey: 
        The apikey supplied by the API service'''
        self.apikey = apikey

    def load_data(self) -> None:
        '''Calls the web api using the required values and stores the response in class data attributes.'''
        if self.apikey is None:
            raise ValueError("The API Key has not been set")
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
            self.weather_data = _download_url(url)
        except:
            pass


def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj

def main() -> None:
    zip = "92697"
    ccode = "US"
    apikey = "65518d2062b2ced79bbb83249bd10638"
    url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip},{ccode}&appid={apikey}"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj['weather'][0]['description'])


if __name__ == '__main__':
    main()