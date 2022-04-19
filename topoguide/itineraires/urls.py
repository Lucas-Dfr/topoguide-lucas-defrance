from django.urls import path

from . import views

app_name = 'itineraires'
urlpatterns = [
    path('',views.liste_itineraires, name = 'Liste des itineraires'),
    path('sorties/<int:itineraire_id>/', views.liste_sorties, name='sorties_liste'),
    path('sortie/<int:sortie_id>/', views.detail_sortie, name='sortie_detail'),
    path('nouvelle_sortie/', views.nouvelle_sortie, name = "sortie_new")
    
]

