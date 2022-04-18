from django.urls import path

from . import views

urlpatterns = [
    path('',views.liste_itineraires, name = 'Liste des itineraires'),
    path('<int:itineraire_id>/', views.liste_sorties, name='Liste des sorties'),
]

