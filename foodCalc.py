# foodscore

typerank = ["meal_delivery",  
"meal_takeaway",
"bar",
"cafe",
"bakery",
"convenience_store",
"grocery_or_supermarket",
"supermarket"]

def FoodScore(location, t = None):
    from googleplaces import GooglePlaces
    import math
    gplaces = GooglePlaces("AIzaSyB1qIvuAxzchC8QWG2Y0nn_9LnYsshrApw")
    rank = 0
    if t != None:
        if t in typerank:
            rank = typerank.index(t) + 1
            mult = (1 + (rank/8))
        else:
            return 0

    query = gplaces.text_search(location = location, radius = 0)
    raw = query.raw_response['results'][0]
    rscore = raw['rating'] * (1+ 1/(1 + math.pow(math.e, -raw['user_ratings_total'])))
    if t == None:
        place = query.places[0]
        place.get_details()
        for t in place.details['types']:
            if t in typerank:
                if typerank.index(t) > rank:
                    rank = typerank.index(t)
        if rank == 0:
            return 0
        mult = (1 + (rank/8))

    return 100/(1 + math.pow(math.e, -(rscore * rank)))
