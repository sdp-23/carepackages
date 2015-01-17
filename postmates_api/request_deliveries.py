import requests 

def main():
    payload = {'dropoff_address':'20 McAllister St, San Francisco, CA 94102','pickup_address':'101 Market St, San Francisco, CA 94105'}
    r = requests.get('https://api.postmates.com/v1/customers/cus_KAeAinGkRksOfF/delivery_quotes', params=payload,auth=('70b3252d-78fa-449f-89b3-3e3278b33c3a', ''))
    print(r.text)


if __name__ == '__main__':
    main()