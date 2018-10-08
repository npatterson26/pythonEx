import urllib.parse
import requests

while True:
    address = input('Address: ')
    if address == 'quit' or address == 'q':
        break

    main_api = 'http://maps.googleapis.com/maps/api/geocode/json?'
    #address = 'omaha'
    url = main_api + urllib.parse.urlencode({'address': address})

    json_data = requests.get(url).json()
    #print(json_data)

    json_status = json_data['status']
    print(url)
    print('API Status: ' + json_status)

    if json_status == 'OK':
        for each in json_data['results'][0]['address_components']:
            print(each['long_name'])


    formatted_address = json_data['results'][0]['formatted_address']
    print()
    print(formatted_address)