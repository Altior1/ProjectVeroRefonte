from django.db import models

# Create your models here.
class Clients(models.Model):
    adresse=models.CharField(max_length=200)
    inscription=models.DateTimeField("Date inscription")
    nom=models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    