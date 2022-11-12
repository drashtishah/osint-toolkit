
def url_format(string: str) -> str:
    '''
    Format a string, so it can be used with an API
    '''
    edited_string = string.strip()
    edited_string = edited_string.replace(' ', "%20")
    return edited_string