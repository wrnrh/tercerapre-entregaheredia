from django.db import models

# Create your models here.

class suscripcion(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()

class betatester(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()

class inscripcion(models.Model):
    nombre= models.CharField(max_length=30)
    email= models.EmailField()
