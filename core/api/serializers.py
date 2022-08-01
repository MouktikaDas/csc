from rest_framework import serializers
from .models import Country,City,State

country_fields = ['id', 'name', 'iso3', 'iso2', 'numeric_code', 'phone_code', 'capital', 'currency', 'currency_name', 'currency_symbol', 'tld', 'native', 'region', 'subregion', 'latitude', 'longitude','emojiU']
state_fields = ['id', 'name', 'state_code', 'latitude', 'longitude', 'type']
city_fields = ['id', 'name', 'latitude', 'longitude']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = country_fields

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = state_fields

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = city_fields