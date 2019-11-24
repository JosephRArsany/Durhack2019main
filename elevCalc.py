pip install -U googlemaps

import googlemaps

gmaps = googlemaps.Client(key = 'AIzaSyB1qIvuAxzchC8QWG2Y0nn_9LnYsshrApw')
geocode_result = gmaps.geocode('Durham Castle, Durham')
source_lat = geocode_result[0]['geometry']['location']['lat']
source_long = geocode_result[0]['geometry']['location']['lng']
source_latlong = str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng'])

def elevation_score(lat, lng):
    elev_dic = {'lat':lat, 'long':lng} #elevation method below only accepts dictionary input 
    my_elev = gmaps.elevation((elev_dic['lat'], elev_dic['long']))
    my_elev_near1 = gmaps.elevation((elev_dic['lat'] + 0.001, elev_dic['long'] + 0.001))
    my_elev_near2 = gmaps.elevation((elev_dic['lat'] - 0.001, elev_dic['long'] + 0.001))
    my_elev_near3 = gmaps.elevation((elev_dic['lat'] - 0.001, elev_dic['long'] - 0.001))
    my_elev_near4 = gmaps.elevation((elev_dic['lat'] + 0.001, elev_dic['long'] - 0.001))
    g1 = my_elev[0]['elevation'] - my_elev_near1[0]['elevation']
    g2 = my_elev[0]['elevation'] - my_elev_near2[0]['elevation']
    g3 = my_elev[0]['elevation'] - my_elev_near3[0]['elevation']
    g4 = my_elev[0]['elevation'] - my_elev_near4[0]['elevation']
    if g1*g2*g3 > 0 and g1*g2*g4 > 0 and g2*g3*g4 > 0: #peak
        result = round(50 + 50*(my_elev[0]['elevation'] + max(g1, g2, g3, g4))/(max(g1, g2, g3, g4) * my_elev[0]['elevation']))
        if result > 100:
            result = 100
    elif g1*g2*g3 < 0 or g1*g2*g4 < 0: #valley
        result = round(100*(max(g1, g2, g3, g4) - min(g1, g2, g3, g4) + my_elev[0]['elevation'])/(max(g1, g2, g3, g4) - min(g1, g2, g3, g4) * my_elev[0]['elevation']))
        if result > 100:
            result = 100
    else: #slope
        result = round(50 + 50*(min(g1, g2, g3, g4) - my_elev[0]['elevation'])/(min(g1, g2, g3, g4) * my_elev[0]['elevation']))
        if result > 100:
            result = 100
    return result






