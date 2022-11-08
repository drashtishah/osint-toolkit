def decimal_degree_coordinates(degree, minutes, seconds, direction):
    '''
    Convert GPS coordinates
    '''
    decimal_degrees = float(degree) + (float(minutes) / 60) + (float(seconds) / 3600)
    if direction == "S" or direction == "W":
        decimal_degrees *= -1
    return decimal_degrees