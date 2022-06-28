from django import forms
from django.db import models
from datetime import datetime


# Create your models here.

class Familiares(models.Model):

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField(null=True)
 

    