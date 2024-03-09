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
from ds_client import send
from WebAPI import WebAPI

class OpenWeather(WebAPI):
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
    
    def load_data(self) -> None:
        '''Calls the web api using the required values and stores the response in class data attributes.'''
        if self.apikey is None:
            raise ValueError("The API Key has not been set")
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.ccode}&appid={self.apikey}"
            self.weather_data = super()._download_url(url)
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
            
    def transclude(self, message:str) -> str:
        '''
  Replaces keywords in a message with associated API data.:param message: The message to transclude
  :returns: The transcluded message
  '''      
        message_list = message.split(' ')
        keyword = [x for x in message_list if "@" in x]
        if keyword == []:
            return False
        for i in keyword:
            if i == '@temperature':
                message = message.replace('@temperature', str(self.temperature))
            elif i == '@hottest':
                message = message.replace('@hottest', str(self.high_temperature))
            elif i == '@coolest':
                message = message.replace('@coolest', str(self.low_temperature))
            elif i == '@longitude':
                message = message.replace('@longitude', str(self.longitude))
            elif i == '@latitude':
                message = message.replace('@latitude', str(self.latitude))
            elif i == '@report':
                message = message.replace('@report', self.description)
            elif i == '@humidity':
                message = message.replace('@humidity', str(self.humidity))
            elif i == '@sunset':
                message = message.replace('@sunset', str(self.sunset))
            elif i == '@sunrise':
                message = message.replace('@sunrise', str(self.sunrise))
            elif i == '@weather':
                message = message.replace('@weather', str(self.description))
        return message
    
def online_posting(message:str):
    username = input("Enter the username : ")
    password = input("Enter the password : ")
    bio = input("Enter a few lines of bio data : ")
    srv_ip = input("Enter the server IP address : ")
    port = "3021"
    send(srv_ip, port, username, password, message, bio)

def weather_main() -> None:
    zip = input("Enter the zip code")
    ccode = input("Enter the country code")
    weather_apikey = "65518d2062b2ced79bbb83249bd10638"
    open_weather = OpenWeather(zip, ccode)
    open_weather.set_apikey(weather_apikey)
    open_weather.load_data()
    print("Keywords that can be used: @temperature, @hottest, @lowest, @longitude, @latitude, @report, @humidity, @sunset, @sunrise, @weather")
    message = input("Enter your message with the keyword")
    message = open_weather.transclude(message)
    online_posting(message)


