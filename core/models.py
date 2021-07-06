from django.db import models

#Clase Obra

class Obra(models.Model):
    idObra = models.IntegerField(primary_key=True, verbose_name='Id')
    nombreObra = models.CharField(max_length=50,verbose_name='Obra')
    nombreArtista = models.CharField(max_length=30,verbose_name='Artista')


    def __str__(self):
        return self.nombreObra

#Clase Concepto

class Concepto(models.Model):
    idConcepto = models.IntegerField(primary_key=True, verbose_name='id')
    nombreConcepto = models.CharField(max_length=50,verbose_name='Concepto')

#Clase Contacto
class Contacto(models.Model):
    idMensajes = models.IntegerField(primary_key=True,verbose_name='id')
    nombreAsuntos = models.CharField(max_length=50, verbose_name='Asunto')
    nombreMensaje = models.CharField(max_length=50,verbose_name='Mensaje')