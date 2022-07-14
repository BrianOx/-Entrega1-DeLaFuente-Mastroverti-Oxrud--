from email.mime import image
from operator import mod
from statistics import mode
from django.db import models

# Create your models here.

class Campeon(models.Model):
    nombre = models.CharField(max_length=50)
    lore = models.TextField()
    imagen_url = models.CharField(max_length=255)

    class Meta:
         verbose_name_plural = "Campeones"

class Item(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.ImageField()

    class Meta:
            verbose_name_plural = "Items"

class Posteo(models.Model):
    titulo = models.CharField(max_length=50)
    cuerpo = models.CharField(max_length=50)
    autor = models.EmailField()
    fecha = models.DateTimeField()

    class Meta:
         verbose_name_plural = "Posteos"