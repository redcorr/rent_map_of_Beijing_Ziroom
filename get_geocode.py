import requests
import pandas

key = '【高德key】'
csv_url = 'rent_info_ori.csv'

source_file = pandas.read_csv(csv_url)
gi = 0
locations = []
geo_codes = []
si = 0
printi = 0
for location in source_file['formatted_block']:
    printi += 1
    if printi % 10 == 0:
        print(str(printi)+'/6356')
    locations.append(location)
    gi = gi + 1
    if gi > 9:
        url_prefix = 'https://restapi.amap.com/v3/geocode/geo?'
        address = locations[0] + '|' + locations[1] + '|' + locations[2] + '|' + locations[3] + '|' + locations[4] + '|' + locations[5] + '|' + locations[6] + '|' + locations[7] + '|' + locations[8] + '|' + locations[9]
        city = '010'
        batch = 'true'
        url = url_prefix+'address='+address+'&city='+city+'&batch='+batch+'&key='+key
        attemps = 0
        while attemps < 10:
            try:
                items = requests.get(url).json()['geocodes']
                break
            except:
                input()
        for i in items:
            geo_code = i['location']
            source_file.loc[si, 'geo_code'] = geo_code
            si = si + 1
        locations = []
        gi = 0
    else:
        continue
source_file.to_csv('rent_info_with_geocode.csv')