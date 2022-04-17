from django.db import models

class Itinineraire(models.Model):
    
    CHOIX_DIFFICULTE = [
        (1,'1 - Très facile'),
        (2,'2 - Facile'),
        (3,'3 - Modérée'),
        (4,'4 - Difficile'),
        (5, '5 - Très difficile'),
    ]
    
    nom = models.CharField('Nom',max_length=200)
    p_dep = models.CharField('Point de départ',max_length=200)
    description = models.CharField('Description de la sortie',max_length=3000)
    alt_dep = models.IntegerField('Altitude de départ')
    altitude_mim = models.IntegerField('Altitude minimale')
    altitude_max = models.IntegerField('Altitude maximale')
    denivele_pos = models.IntegerField('Denivelé positif cumulé')
    denivele_neg = models.IntegerField('Denivelé negatif cumulé')
    duree = models.TimeField('Durée estimée',auto_now=False, auto_now_add=False)
    difficulte = models.IntegerField('Difficulté estimée', choices = CHOIX_DIFFICULTE)
    
    
