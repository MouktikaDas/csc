from api.models import Country, City, State
import json
import time
country_list = []
state_list = []
city_list = []

country_fields = ['id', 'name', 'iso3', 'iso2', 'numeric_code', 'phone_code', 'capital', 'currency', 'currency_name', 'currency_symbol', 'tld', 'native', 'region', 'subregion', 'latitude', 'longitude', 'emoji', 'emojiU']
state_fields = ['id', 'name', 'state_code', 'latitude', 'longitude', 'type']
city_fields = ['id', 'name', 'latitude', 'longitude']


def read_json(json_path="./csc.json"):
    return json.loads(open(json_path, encoding='utf-8').read())


def run():
    t1 = time.time()
    data = read_json('./static/countries+states+cities.json')
    print(city_fields)
    for country in data:
        cf = list(map(country.get, country_fields))
        cf = dict(zip(country_fields,cf))
        country_list.append(cf)
        for state in country['states']:
            sf = list(map(state.get,state_fields))
            sf = dict(zip(state_fields,sf))
            sf['country_id'] = country['id']
            state_list.append(sf)
            for city in state['cities']:
                cif = list(map(city.get,city_fields))
                cif = dict(zip(city_fields,cif))
                cif['country_id'] = country['id']
                cif['state_id'] = state['id']
                city_list.append(cif)
    t2 = time.time()
    print("time:",t2-t1)
    with open("countries.txt",'w', encoding="utf-8") as f1:
        print(country_list,file=f1)
    with open("states.txt",'w', encoding="utf-8") as f2:
        print(state_list,file=f2)
    with open("cities.txt",'w', encoding="utf-8") as f3:
        print(city_list,file=f3)

    



# python manage.py runscript import_from_json
