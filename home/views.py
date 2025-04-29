from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
import googlemaps
from studySpot import settings

from .models import Locations

class HomeView(ListView):
    template_name = "home/index.html"
    context_object_name = 'mydata'
    model = Locations
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_data'] = {'title': 'Study Spot'}
        return context

class GeocodingView(View):
    template_name = "home/geocoding.html"

    def get(self, request, pk):
        location = Locations.objects.get(pk=pk)

        if location.lng and location.lat and location.place_id != None:
            lat = location.lat
            lng = location.lng
            place_id = location.place_id
            label = "from my database"

        elif location.address and location.country and location.zipcode and location.city != None:
            address_string = str(location.address) + ", " + str(location.zipcode) + ", " + str(
                location.city) + ", " + str(location.country)

            gmaps = googlemaps.Client(key=settings.GOOGLE_API_KEY)
            result = gmaps.geocode(address_string)[0]

            lat = result.get('geometry', {}).get('location', {}).get('lat', None)
            lng = result.get('geometry', {}).get('location', {}).get('lng', None)
            place_id = result.get('place_id', {})
            label = "from my api call"

            location.lat = lat
            location.lng = lng
            location.place_id = place_id
            location.save()

        else:
            result = ""
            lat = ""
            lng = ""
            place_id = ""
            label = "no call made"

        context = {
            'location': location,
            'lat': lat,
            'lng': lng,
            'place_id': place_id,
            'label': label
        }
        return render(request, self.template_name, context)

class MapView(View):
    template_name = "home/map.html"

    def get(self,request):
        key = settings.GOOGLE_API_KEY
        eligable_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []

        for a in eligable_locations:
            data = {
                'lat': float(a.lat),
                'lng': float(a.lng),
                'name': a.name,
                'spots' : str(a.spots),
                "location": a.location,
            }

            locations.append(data)


        context = {
            "key":key,
            "locations": locations
        }

        return render(request, self.template_name, context)
