from PIL import Image

# TO DO: Add a tool for editing GPS coordinates in images
# https://github.com/python-pillow/Pillow/issues/6657

# People whose code helped me write this code
# David Bombal: https://github.com/davidbombal/red-python-scripts/blob/main/remove_exif.py

def metadata(filepath, new_filename):
    '''
    Input: filepath
    Output: image without EXIF data (inside output folder)
    '''
    img = Image.open(filepath)
    img_data = list(img.getdata())
    edit_img = Image.new(img.mode, img.size)
    edit_img.putdata(img_data)
    edit_img.save(f'output/{new_filename}')
    return edit_img