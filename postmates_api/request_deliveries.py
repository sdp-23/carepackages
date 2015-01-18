import requests 

def main():
    payload = {
               'manifest':"a box of kittens",
               'pickup_name':"The Warehouse",
               'pickup_address':"20 McAllister St, San Francisco, CA",
               'pickup_phone_number':"555-555-5555",
               'pickup_business_name':"Optional Pickup Business Name, Inc.",
               'pickup_notes':"Optional note that this is Invoice #123",
               'dropoff_name':"Alice",
               'dropoff_address':"101 Market St, San Francisco, CA",
               'dropoff_phone_number':"415-555-1234",
               'dropoff_business_name':"Optional Dropoff Business Name, Inc.",
               'dropoff_notes':"Optional note to ring the bell",
               'quote_id':'dqt_KAfHlMtm4ZWrhV'
               
    }
    r = requests.post('https://api.postmates.com/v1/customers/cus_KAeAinGkRksOfF/deliveries',data=payload, auth=('70b3252d-78fa-449f-89b3-3e3278b33c3a',''))
    print(r.text)
    print("done!!")


if __name__ == '__main__':
    main()