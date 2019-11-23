pip install -U googlemaps

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyB1qIvuAxzchC8QWG2Y0nn_9LnYsshrApw')
geocode_result = gmaps.geocode('Elvet Hill, Durham')
source_lat = geocode_result[0]['geometry']['location']['lat']
source_long = geocode_result[0]['geometry']['location']['lng']
source_latlong = str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng'])

elev_dic = {'lat':source_lat, 'long':source_long}
my_elev = gmaps.elevation((elev_dic['lat'], elev_dic['long']))
print(my_elev)



