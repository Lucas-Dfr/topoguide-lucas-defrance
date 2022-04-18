# Generated by Django 4.0.3 on 2022-04-17 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itineraires', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itineraire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, verbose_name='Nom')),
                ('p_dep', models.CharField(max_length=200, verbose_name='Point de départ')),
                ('description', models.TextField(verbose_name='Description de la sortie')),
                ('alt_dep', models.IntegerField(verbose_name='Altitude de départ')),
                ('altitude_min', models.IntegerField(verbose_name='Altitude minimale')),
                ('altitude_max', models.IntegerField(verbose_name='Altitude maximale')),
                ('denivele_pos', models.IntegerField(verbose_name='Denivelé positif cumulé')),
                ('denivele_neg', models.IntegerField(verbose_name='Denivelé negatif cumulé')),
                ('duree', models.DurationField(verbose_name='Durée estimée')),
                ('difficulte', models.IntegerField(choices=[(1, '1 - Très facile'), (2, '2 - Facile'), (3, '3 - Modérée'), (4, '4 - Difficile'), (5, '5 - Très difficile')], verbose_name='Difficulté estimée')),
            ],
        ),
        migrations.DeleteModel(
            name='Itinineraire',
        ),
    ]
