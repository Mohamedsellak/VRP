from math import radians, cos, sin, asin, sqrt
def haversine_distance(loc1, loc2):
    """
    Calculate the Haversine distance between two locations in kilometers.
    """
    lat1, lon1 = loc1
    lat2, lon2 = loc2
    # convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # radius of earth in kilometers is 6371
    km = 6371 * c
    return km

def total_distance(route, locations):
    """
    Calculate the total distance traveled for a given route.
    """
    dist = 0
    for i in range(len(route)-1):
        loc1 = locations[route[i]]
        loc2 = locations[route[i+1]]
        dist += haversine_distance(loc1, loc2)
    return dist

#swap method
def swap(route, i, j):
    route[i], route[j] = route[j], route[i]
