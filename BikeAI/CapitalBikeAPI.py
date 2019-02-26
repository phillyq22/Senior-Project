import requests
import os
import logging
import json
from datetime import datetime





def get_data_from_api():
    ''' Get data from api.
        Make sure to return data, last_updated, and ttl '''
    url = 'https://gbfs.capitalbikeshare.com/gbfs/en/station_status.json'
    response = requests.get(url)
    # if response is not good, raise error
    response.raise_for_status()
    return response.json()

x = get_data_from_api()

##def separate_list(x):



##print(get_data_from_api()['data']['stations'][0]['num_bikes_available'])
##print(separate_list(x))
print(x)


##print(get_data_from_api())