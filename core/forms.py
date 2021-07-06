from django import forms
from django.db import models
from django.db.models import fields
from django.forms import ModelForm
from .models import Obra
from .models import Contacto



class ObraForm(ModelForm):
    class Meta:
        model = Obra
        fields = ['idObra','nombreObra','nombreArtista']

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['idMensajes','nombreAsuntos', 'nombreMensaje']