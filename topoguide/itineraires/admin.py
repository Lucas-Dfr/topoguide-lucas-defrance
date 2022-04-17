from django.contrib import admin

from .models import Itineraire

class ItineraireAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Description générale', {'fields': ('nom','duree','difficulte','description')}),
        ('Informations complémentaires', {'fields': ('p_dep','alt_dep','altitude_min','altitude_max','denivele_pos','denivele_neg')}),
    ]

admin.site.register(Itineraire, ItineraireAdmin)