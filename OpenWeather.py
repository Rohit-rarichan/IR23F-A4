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
    def __init__(self, zipcode:str, ccode:str) -> None:
        self.zipcode = zipcode
        self.ccode = ccode
        self.apikey = None
        self.weather_data = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None 
        self.latitude = None 
        self.longitude = None 
        self.description = None 
        self.humidity = None 
        self.sunset = None 
        self.sunrise = None 
    
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
            self.temperature = self.weather_data['main']['temp']
            self.high_temperature = self.weather_data['main']['temp_max']
            self.low_temperature = self.weather_data['main']['temp_min']
            self.longitude = self.weather_data['coord']['lon']
            self.latitude = self.weather_data['coord']['lat']
            self.description = self.weather_data['weather'][0]['description']
            self.humidity = self.weather_data['main']['humidity']
            self.sunset = self.weather_data['sys']['sunset']
            self.sunrise = self.weather_data['sys']['sunrise']
        except urllib.error.URLError as e:
            raise ValueError(f"Failed to connect to OpenWeather API")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise ValueError("Requested remote API is unavailable")
            elif e.code == 503:
                raise ValueError("The API source listed is not currently working")
            else:
                raise ValueError("HTTP ERROR:", e.code)

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
    weather_apikey = "65518d2062b2ced79bbb83249bd10638"
    open_weather = OpenWeather(zip, ccode)
    open_weather.set_apikey(weather_apikey)
    open_weather.load_data()


if __name__ == '__main__':
    main()