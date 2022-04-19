from django.urls import path

from . import views

urlpatterns = [
    path('',views.liste_itineraires, name = 'Liste des itineraires'),
    path('sorties/<int:itineraire_id>/', views.liste_sorties, name='Liste des sorties'),
    path('sortie/<int:sortie_id>/', views.detail_sortie, name='Détail de la sortie'),
    
]

