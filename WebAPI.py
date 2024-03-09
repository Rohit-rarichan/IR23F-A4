# webapi.py

# Starter code for assignment 4 in ICS 32
# Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan
# rraricha@uci.edu
# 36126645

from abc import ABC, abstractmethod
import json, urllib
from urllib import request,error

class WebAPI(ABC):
  def set_apikey(self, apikey:str) -> None:
       self.apikey = apikey

  def _download_url(self, url: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj    

  @abstractmethod
  def load_data(self):
    pass

  @abstractmethod
  def transclude(self, message:str) -> str:
    pass
