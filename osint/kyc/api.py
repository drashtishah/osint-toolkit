import pandas as pd
import requests
from .utils import *

def open_corporates(COMPANY_NAME):
    COMPANY_NAME = url_format(COMPANY_NAME)
    BASE_URL = 'https://api.opencorporates.com/v0.4/companies/search?q='
    response = requests.get(f'{BASE_URL}{COMPANY_NAME}')
    if response:
        data = response.json()
        return data
    else:
        print(f'Something is wrong with the API')
        print(f'Check this API endpoint: {BASE_URL}{COMPANY_NAME}')
        return None