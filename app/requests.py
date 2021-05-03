import urllib.request,json
from datetime import datetime


# Getting the movie base url
base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_URL']


def get_quote():
    '''Function to that gets the json response to our url request'''
    
    with urllib.request.urlopen(base_url) as url:
        get_quote_data = url.read()
        get_quote_response = json.loads(get_quote_data)
    
    return get_quote_response
  
