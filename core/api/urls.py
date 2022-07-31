from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns =[
    path('country/', views.CountryList.as_view()),
    path('state/<int:country>/', views.StateList.as_view()),
    path('city/<int:state>/', views.CityList.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)