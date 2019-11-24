import googlemaps

RADIUS = 10000
API_KEY = 'AIzaSyB1qIvuAxzchC8QWG2Y0nn_9LnYsshrApw'

gmaps = googlemaps.Client(key = API_KEY)

with open("gmapsAPItypelist.txt", "r") as file:
    TypeList = list(file.read().split("\n"))


def WDistance(l1, l2):
    l1tol2 = gmaps.directions(l1, l2, mode = "walking")
    return l1tol2[0]['legs'][0]['duration']['text']


currentlocation = gmaps.geolocate()

search_results = []

for t in TypeList:
    temp = gmaps.places_nearby(location = currentlocation['location'], radius = RADIUS, type = t)['results']
    for i in temp:
        search_results.append((i['name'], i['geometry']['location']))

with open("places.txt", "w") as placefile:
    placefile.write(str(search_results))
    

