from django.forms import ModelForm
from itineraires.models import Sortie, Itineraire
from django import forms

class NewSortieForm(ModelForm):
    """
    Form made to create a new excursion
    """
    class Meta:
        model = Sortie
        fields = ['itineraire', 'date', 'duree_reelle', 'nb_personnes', 'experience', 'meteo', 'difficulte']
        labels = {
            'itineraire': 'Itinéraire',
            'date': 'Date de la sortie',
            'duree_reelle': 'Durée réelle de la sortie',
            'nb_personnes': 'Nombre de personnes',
            'experience': 'Expérience du groupe',
            'meteo': 'Météo',
            'Difficulte': 'Difficultée ressentie',
        }
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

class UpdateSortieForm(ModelForm):
    """
    Same form as above but the field "itinerary" has been removed since a user 
    cannot change the itinerary corresponding to his excursion
    """
    class Meta:
        model = Sortie
        fields = ['date', 'duree_reelle', 'nb_personnes', 'experience', 'meteo', 'difficulte']
        labels = {
            'date': 'Date de la sortie',
            'duree_reelle': 'Durée réelle de la sortie',
            'nb_personnes': 'Nombre de personnes',
            'experience': 'Expérience du groupe',
            'meteo': 'Météo',
            'Difficulte': 'Difficultée ressentie',
        }
        widgets = {
        'date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }
