from django.urls import path
from .views import HomeView
from .views import GeocodingView
from .views import MapView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('geocoding/<int:pk>', GeocodingView.as_view(), name='my_geocoding_view'),
    path('map', MapView.as_view(), name='my_map_view'),
]
