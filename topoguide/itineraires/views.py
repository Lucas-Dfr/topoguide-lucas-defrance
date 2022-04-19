from multiprocessing import context
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Itineraire, Sortie

@login_required()
def liste_itineraires(request):
    itineraries_list = Itineraire.objects.order_by("nom")
    context = {'itineraries_list' : itineraries_list }
    return render(request, 'itineraires/liste_itineraires.html', context)

@login_required()
def liste_sorties(request,itineraire_id):
    iti = Itineraire.objects.get(pk=itineraire_id)
    exursions_list = Sortie.objects.filter(itineraire = iti)
    context = {'excursions_list' : exursions_list, 'iti' : iti}
    return render(request,'itineraires/sorties.html',context)

@login_required()
def detail_sortie(request,sortie_id):
    sortie = Sortie.objects.get(pk=sortie_id)
    context = {'sortie' : sortie}
    return render(request,'itineraires/detail_sortie.html',context)
     