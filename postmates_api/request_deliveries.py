import requests 
import carepackages.models


def make_delivery(package, to_address):
    # first setting the quote
    #to_address = "20 McAllister St, San Francisco, CA 94102"
    
    # getting from_address    
    r_geo = requests.post('https://maps.googleapis.com/maps/api/geocode/json?address='+to_address+'&key=AIzaSyDMVxOgRUivjM8LrwE_BxNpxmd8-DmysGs')
    lat = r_geo.json().get('results').pop(0).get('geometry').get('location').get('lat')
    long = r_geo.json().get('results').pop(0).get('geometry').get('location').get('lng')
    city = r_geo.json().get('results').pop(0).get('address_components').pop(3).get('long_name')
    store_name = package.name
    r_places = requests.post('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+str(lat)+','+str(long)+'&name='+store_name+'&keyword='+city+'&radius=16000&key=AIzaSyAwvfiyJj3KhgdH9y-PR2dYZQ1o7neyZ6k')
    store_address= r_places.json().get('results').pop(0).get('vicinity')    
    
    # getting quote
    payload_q = {"pickup_address": store_address,"dropoff_address": to_address}
    r = requests.post('https://api.postmates.com/v1/customers/cus_KAeAinGkRksOfF/delivery_quotes',data=payload_q, 
                     auth=('70b3252d-78fa-449f-89b3-3e3278b33c3a',''))
    quote_id = r.json().get('id')
        
    # setting the delivery request
    payload_d = {
              'manifest':"a box of kittens",
              'pickup_name':"The Warehouse",
              'dropoff_address':"20 McAllister St, San Francisco, CA",
              'pickup_phone_number':"555-555-5555",
              'pickup_business_name':"Optional Pickup Business Name, Inc.",
              'pickup_notes':"Optional note that this is Invoice #123",
              'dropoff_name':"Alice",
              'pickup_address':store_address,
              'dropoff_phone_number':"415-555-1234",
              'dropoff_business_name':"Optional Dropoff Business Name, Inc.",
              'dropoff_notes':"Optional note to ring the bell",
              'quote_id':quote_id
               
    }
    r = requests.post('https://api.postmates.com/v1/customers/cus_KAeAinGkRksOfF/deliveries',data=payload_d, auth=('70b3252d-78fa-449f-89b3-3e3278b33c3a',''))
    print(store_address)
    print(r.text)


def main():
    make_delivery(package, to_address)


if __name__ == '__main__':
    main()