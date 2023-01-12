# import requests library
import requests 
import json
# import plotting library
import matplotlib
import matplotlib.pyplot as plt 
from datetime import date, datetime, timedelta
import pandas as pd
import numpy as np

def recull_dades():
    endpoint = 'https://apidatos.ree.es'
    get_archives = '/en/datos/mercados/precios-mercados-tiempo-real'
    headers = {'Accept': 'application/json',
               'Content-Type': 'application/json',
               'Host': 'apidatos.ree.es'}
    params = {'start_date': '2023-01-02T00:00', 'end_date': '2023-01-02T23:00', 'time_trunc':'hour'}
    response = requests.get(endpoint+get_archives, headers=headers, params=params)
    json = response.json()
    return json