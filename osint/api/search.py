import pandas as pd
import requests
from .utils import url_format

def lei_by_legal_name(legal_name: str):
    '''
    Use GLEIF API to search by legal name
    '''
    legal_name = url_format(legal_name)
    base_url: str = 'https://api.gleif.org/api/v1/lei-records?filter[entity.legalName]='
    response = requests.get(f'{base_url}{legal_name}')
    if response:
        data = response.json()
        return data
    print('Something is wrong with the API')
    print(f'Check this API endpoint: {base_url}{legal_name}')
    return None