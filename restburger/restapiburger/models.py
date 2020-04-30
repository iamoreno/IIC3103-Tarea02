from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# Create your models here.

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)

class Hamburguesa(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=255)
    imagen = models.CharField(max_length=255)
    ingredientes = models.ManyToManyField(Ingrediente, blank=True)


