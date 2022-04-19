from multiprocessing import context
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import itineraires
from .form import ExcursionForm

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

@login_required()
def nouvelle_sortie(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExcursionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect('itineraires:sorties_liste')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExcursionForm()

    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})
