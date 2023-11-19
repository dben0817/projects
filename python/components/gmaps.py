import googlemaps

def get_commute_duration():
    
    home_address = "" # Enter your home address
    work_address = "" # Enter your work address
    
    # Create an API key at the Google Developers website
    google_maps_api = ""
    gmaps = googlemaps.Client(key=google_maps_api)
    
    directions = gmaps.directions(home_address, work_address)
    first_leg = directions[0]['legs'][0]
    duration = first_leg['duration']['text']
    
    return duration