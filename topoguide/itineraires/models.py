from django.db import models
from django.contrib.auth.models import User

class Itineraire(models.Model):
    
    CHOIX_DIFFICULTE = [
        (1,'1 - Très facile'),
        (2,'2 - Facile'),
        (3,'3 - Modérée'),
        (4,'4 - Difficile'),
        (5, '5 - Très difficile'),
    ]
    
    nom = models.CharField('Nom',max_length=200)
    p_dep = models.CharField('Point de départ',max_length=200)
    description = models.TextField('Description de la sortie')
    alt_dep = models.IntegerField('Altitude de départ')
    altitude_min = models.IntegerField('Altitude minimale')
    altitude_max = models.IntegerField('Altitude maximale')
    denivele_pos = models.IntegerField('Denivelé positif cumulé')
    denivele_neg = models.IntegerField('Denivelé negatif cumulé')
    duree = models.DurationField('Durée estimée')
    difficulte = models.IntegerField('Difficulté estimée', choices = CHOIX_DIFFICULTE)
    
    def __str__(self):
        return self.nom

class Sortie(models.Model):
    
    CHOIX_EXPERIENCE = [
        ('Tous débutants','Tous débutants'),
        ('Groupe mixte','Groupe mixte'),
        ('Tous expérimentés','Tous expérimentés'),
    ]
    
    CHOIX_METEO = [
        ('Mauvaise','Mauvaise'),
        ('Moyenne','Moyenne'),
        ('Bonne','Bonne'),
    ]
    
    CHOIX_DIFFICULTE = [
        (1,'1 - Très facile'),
        (2,'2 - Facile'),
        (3,'3 - Modérée'),
        (4,'4 - Difficile'),
        (5, '5 - Très difficile'),
    ]
    
    
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE)
    date = models.DateField("Date de la sortie")
    duree_reelle = models.DurationField('Durée réelle de la sortie')
    nb_personnes = models.IntegerField('Nombre de personnes ayant participé à la sortie',default=1)
    experience = models.CharField("Experience du groupe", max_length=50 ,choices = CHOIX_EXPERIENCE)
    meteo = models.CharField(max_length=50,choices = CHOIX_METEO)
    difficulte = models.IntegerField('Difficulté ressentie', choices = CHOIX_DIFFICULTE)
    
