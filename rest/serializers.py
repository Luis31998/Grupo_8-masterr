from rest_framework import fields, serializers
from core.models import Contacto, Obra

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = ['idObra','nombreObra','nombreArtista']

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model: Contacto
        fields = ['idMensajes','nombreAsuntos', 'nombreMensaje']