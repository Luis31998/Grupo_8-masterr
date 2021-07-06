from django.urls import path
from .views import Contactos, EditarObras, eliminarObras, index
from .views import Obras
from .views import nuevaObras
from .views import Contacto
from .views import EditarObras
from .views import eliminarObras


urlpatterns = [
    path('', index,name="index"),
    path('Obras/listar', Obras, name='Obras'),
    path('Obras/Agregar' , nuevaObras, name='nuevaObras'),
    path('contactos/', Contactos, name='contactos'),
    path('Obras/editar/<id>',EditarObras, name='EditarObras'),
    path('Obras/eliminar/<id>',eliminarObras,name="eliminarObras")
    
]