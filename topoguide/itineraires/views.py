from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Itineraire

def liste_itineraires(request):
    itineraries_list = Itineraire.objects.order_by("nom")
    context = {'itineraries_list' : itineraries_list }
    return render(request, 'itineraires/liste_itineraires.html', context)

def liste_sorties(request,itineraire_id):
    response = "Bientôt ici, les sorties de l'itineraire %s."
    return HttpResponse(response % itineraire_id)
     