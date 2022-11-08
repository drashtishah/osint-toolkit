from PIL import Image
from PIL.ExifTags import GPSTAGS, TAGS
import pandas as pd

from .utils import *

# People whose code helped me write this code
# David Bombal: https://github.com/davidbombal/red-python-scripts/blob/main/exif.py

def extract_GPSInfo(dictionary):
    '''
    Extract data from GPSInfo and convert to decimal degrees
    '''
    data = {GPSTAGS.get(tag): value for tag, value in dictionary.items()}
    lat_degree, lat_minutes, lat_seconds = data['GPSLatitude'][0], data['GPSLatitude'][1], data['GPSLatitude'][2]
    long_degree, long_minutes, long_seconds = data['GPSLongitude'][0], data['GPSLongitude'][1], data['GPSLongitude'][2]
    lat_ref, long_ref = data['GPSLatitudeRef'], data['GPSLongitudeRef']
    lat = decimal_degree_coordinates(lat_degree, lat_minutes, lat_seconds, lat_ref)
    long = decimal_degree_coordinates(long_degree, long_minutes, long_seconds, long_ref)
    return lat, long

def exif(filepath):
    '''
    EXIF stands for Exchangeable Image File format
    Input: filepath
    Output: dictionary of EXIF data
    '''
    try:
        img = Image.open(filepath)
    except FileNotFoundError:
        print(f'Check your filename')
        return None
    
    if img._getexif() == None:
        print(f'{filepath} contains no EXIF data')
        return None
    else:
        data = {TAGS.get(tag): value for tag, value in img._getexif().items()}
        df = pd.Series(data)
        if 'GPSInfo' in df.index:
            gps_data = df.loc['GPSInfo']
            lat, long = extract_GPSInfo(gps_data)
            df.loc['Latitude'] = lat
            df.loc['Longitude'] = long
            df.loc['Google Maps URL'] = f'https://maps.google.com/?q={lat},{long}'
        return df