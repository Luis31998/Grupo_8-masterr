from django.urls import path
from .views import detalle_obras, lista_obras
from .viewslogin import login

urlpatterns = [
    path('obra/listar', lista_obras, name='lista_obras'),
    path('obra/detalle/<id>', detalle_obras, name="detalle_obras"),
    path('login',login, name="login"),
]