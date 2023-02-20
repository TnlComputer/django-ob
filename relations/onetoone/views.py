from django.shortcuts import render
from django.http import HttpResponse
from .models import Place, Restaurant


def create(request):
    place = Place(name="Lugar 1", address='calle demo')
    place.save()

    restaurant = Restaurant(place=place, number_employees=8)
    restaurant.save()
    return HttpResponse(restaurant.place.name)


def delete(request):
    Place.objects.filter(id=2).delete()
    return HttpResponse("eliminado lugar")
