from django.contrib import admin

from .models import Itineraire, Sortie

class ItineraireAdmin(admin.ModelAdmin):
    # Register itinerary models and order them in coherent fields
    fieldsets = [
        ('Description générale', {'fields': ('nom','duree','difficulte','description')}),
        ('Informations complémentaires', {'fields': ('p_dep','alt_dep','altitude_min','altitude_max','denivele_pos','denivele_neg')}),
    ]

admin.site.register(Itineraire, ItineraireAdmin)

class SortieAdmin(admin.ModelAdmin):
    # Register excursion models and diplay only the key information
    list_display = ('utilisateur','itineraire', 'date')

admin.site.register(Sortie, SortieAdmin)