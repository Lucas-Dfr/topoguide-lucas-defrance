from django.forms import ModelForm
from itineraires.models import Sortie, Itineraire
from django.utils.translation import gettext_lazy as _

class ExcursionForm(ModelForm):
    class Meta:
        model = Sortie
        fields = ['utilisateur', 'itineraire', 'date', 'duree_reelle', 'nb_personnes', 'experience', 'meteo', 'difficulte']
        labels = {
            'utilisateur': _('Par'),
            'itineraire': _('Itinéraire'),
            'date': _('Date de la sortie'),
            'duree_reelle': _('Durée réelle de la sortie'),
            'nb_personnes': _('Nombre de personnes'),
            'experience': _('Expérience du groupe'),
            'meteo': _('Météo'),
            'Difficulte': _('Difficultée ressentie'),
        }