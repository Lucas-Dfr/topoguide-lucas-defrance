from django.forms import ModelForm
from itineraires.models import Sortie, Itineraire
from django import forms

class SortieForm(ModelForm):
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