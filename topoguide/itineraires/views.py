from multiprocessing import context
from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import NewSortieForm, UpdateSortieForm

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
        form = NewSortieForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.instance.utilisateur = request.user
            sortie_iti = form.cleaned_data['itineraire'] # The redirection will use the itinerary id
            form.save()
            # redirect to a new URL:
            return redirect('itineraires:sorties_liste', itineraire_id = sortie_iti.id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewSortieForm()

    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})

@login_required()
def modif_sortie(request, sortie_id):
    """
    Update an existing excursion based on user input in form
    
    Args:
        request: the incoming request, GET or POST
        sortie_id: the database ID of the excursion to update
        
    Returns:
        - a page with a pre-filled form if it was a GET request,
        - a page with a pre-filled form if it was a POST request
          with invalid data,
        - or the list of excursions if it was a POST with valid data
    """
    # Fist get data from the database
    sortie = Sortie.objects.get(pk=sortie_id)
    
    # The user logged-in can only edit his own excursions
    ref_user = sortie.utilisateur
    if ref_user != request.user:
        messages.error(request, ('Oups, vous ne pouvez modifier que vos propres sorties'))
        return redirect('itineraires:sorties_liste', itineraire_id = sortie.itineraire.id)
    
    if request.method == 'GET':
        form = UpdateSortieForm(instance=sortie)
        
    elif request.method == 'POST':
        form = UpdateSortieForm(request.POST, instance=sortie)
        if form.is_valid():
            form.save()
            sortie_iti = form.cleaned_data['itineraire']
            return redirect('itineraires:sorties_liste', itineraire_id = sortie_iti.id)
        
    return render(request,'itineraires/modif_sortie.html', {'form': form})
    
    