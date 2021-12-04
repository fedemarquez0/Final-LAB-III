from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, PROTECT
from django.db.models.fields.related import OneToOneField

# Create your models here.

class Estante(models.Model):
    estante = models.CharField(max_length=50)

class Variedad(models.Model):
    variedad = models.CharField(max_length=50)

class Origen(models.Model):
    origen = models.CharField(max_length=50)

class Bodega(models.Model):
    bodega = models.CharField(max_length=50)

class Vino(models.Model):
    nombre = models.CharField(max_length=100)
    bodega = models.ForeignKey(Bodega, on_delete=CASCADE)
    variedad = models.ForeignKey(Variedad, on_delete=CASCADE)
    cosecha = models.DateField()
    origen = models.ForeignKey(Origen, on_delete=CASCADE)
    cantidad = models.PositiveSmallIntegerField()
    codigo = models.BigIntegerField()
    precio = models.FloatField()
    estante = models.ForeignKey(Estante, on_delete=CASCADE)
    imagen = models.ImageField(upload_to="catalogo/") #se van a guardar en media/catalogo

class Comentario(models.Model):
    ojo = models.PositiveSmallIntegerField(max_length=10)
    nariz = models.PositiveSmallIntegerField(max_length=10)
    boca = models.PositiveSmallIntegerField(max_length=10)
    equilibrio_armonia = models.PositiveSmallIntegerField(max_length=10)
    nota = models.TextField()
    vino = OneToOneField(Vino,on_delete=PROTECT)

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    fecha_baja = models.DateField()

