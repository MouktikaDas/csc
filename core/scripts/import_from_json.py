from api.models import Country, City, State
import json
import time
country_list = []
state_list = []
city_list = []

country_fields = ['id', 'name', 'iso3', 'iso2', 'numeric_code', 'phone_code', 'capital', 'currency', 'currency_name', 'currency_symbol', 'tld', 'native', 'region', 'subregion', 'latitude', 'longitude','emojiU']
state_fields = ['id', 'name', 'state_code', 'latitude', 'longitude', 'type']
city_fields = ['id', 'name', 'latitude', 'longitude']


def read_json(json_path="./csc.json"):
    return json.loads(open(json_path, encoding='utf-8').read())


def run():
    t1 = time.time()
    data = read_json('./static/countries+states+cities.json')
    for country in data:
        cf = list(map(country.get, country_fields))
        cf = dict(zip(country_fields,cf))
        country_list.append(cf)
        for state in country['states']:
            sf = list(map(state.get,state_fields))
            sf = dict(zip(state_fields,sf))
            sf['country_id_id'] = country['id']
            state_list.append(sf)
            for city in state['cities']:
                cif = list(map(city.get,city_fields))
                cif = dict(zip(city_fields,cif))
                cif['state_id_id'] = state['id']
                cif['country_id_id'] = country['id']
                city_list.append(cif)
    countryl = [Country(**data_dict) for data_dict in country_list]
    countries = Country.objects.bulk_create(countryl)
    statel = [State(**data_dict) for data_dict in state_list]
    states = State.objects.bulk_create(statel)
    cityl = [City(**data_dict) for data_dict in city_list]
    cities = City.objects.bulk_create(cityl)
    t2 = time.time()
    print("time:",t2-t1)






# python manage.py runscript import_from_json
