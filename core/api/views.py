from django.shortcuts import render
from rest_framework.views import APIView
from .models import Country, City, State
from .serializers import CountrySerializer, StateSerializer, CitySerializer
from rest_framework.response import Response
from django.http import Http404

# Create your views here.


class CountryList(APIView):
    """
    List all countries.
    """

    def get(self, request, format=None):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class StateList(APIView):
    """
    List all states in a country.
    """

    def get_objects(self, country):
        try:
            return State.objects.filter(country_id=country)
        except State.DoesNotExist:
            raise Http404

    def get(self, request, country, format=None):
        states = self.get_objects(country)
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data)

class CityList(APIView):
    """
    List all cities in a state.
    """
    def get_objects(self, state):
        try:
            return City.objects.filter(state_id=state)
        except City.DoesNotExist:
            raise Http404

    def get(self, request, state, format=None):
        cities = self.get_objects(state)
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)
