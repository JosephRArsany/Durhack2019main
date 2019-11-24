#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install -U googlemaps


# In[2]:


import googlemaps


# In[35]:


gmaps = googlemaps.Client(key = 'AIzaSyB1qIvuAxzchC8QWG2Y0nn_9LnYsshrApw')
geocode_result = gmaps.geocode('Grey College, Durham')
source_lat = geocode_result[0]['geometry']['location']['lat']
source_long = geocode_result[0]['geometry']['location']['lng']
source_latlong = str(geocode_result[0]['geometry']['location']['lat']) + ',' + str(geocode_result[0]['geometry']['location']['lng'])


# In[36]:


elev_dic = {'lat':source_lat, 'long':source_long}
my_elev = gmaps.elevation((elev_dic['lat'], elev_dic['long']))
my_elev_near1 = gmaps.elevation((elev_dic['lat'] + 0.001, elev_dic['long'] + 0.001))
my_elev_near2 = gmaps.elevation((elev_dic['lat'] - 0.001, elev_dic['long'] + 0.001))
my_elev_near3 = gmaps.elevation((elev_dic['lat'] - 0.001, elev_dic['long'] - 0.001))
my_elev_near4 = gmaps.elevation((elev_dic['lat'] + 0.001, elev_dic['long'] - 0.001))
grad1 = my_elev[0]['elevation'] - my_elev_near1[0]['elevation']
grad2 = my_elev[0]['elevation'] - my_elev_near2[0]['elevation']
grad3 = my_elev[0]['elevation'] - my_elev_near3[0]['elevation']
grad4 = my_elev[0]['elevation'] - my_elev_near4[0]['elevation']
print(grad1, grad2, grad3, grad4, (grad1 + grad2 + grad3 + grad4)/4)


# In[ ]:




