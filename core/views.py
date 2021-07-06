from django import forms
from django.shortcuts import redirect, render
from .models import Obra
from .forms import ObraForm
from .forms import ContactoForm
from .models import Contacto

def index(request):
    return render(request, 'core/index.html')

def Contactos (request):
    Contacto = ContactoForm()
    
    datos={

        'form' : Contacto
        
    }
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje'] = 'Obra Creada Exitosamente'

    return render(request, 'core/Contactos.html',datos)

def Obras(request):
    Obras = Obra.objects.all()

    datos={
        'Obras' : Obras
    }

    return render(request, 'core/Obras.html',datos)

def nuevaObras(request):
    form= ObraForm()
    
    datos = {
        'form' : form
    }
    if request.method == 'POST':
        form = ObraForm (request.POST)
        if form.is_valid:
            form.save()
            datos['mensaje'] = 'Obra Creada Exitosamente'
            
    return render(request, 'core/nuevaObras.html',datos)

def EditarObras(request,id):

    Obras= Obra.objects.get(idObra=id)

    datos= {
        'form': ObraForm(instance=Obras)
    }

    if request.method == 'POST':
        formulario = ObraForm(data=request.POST, instance=Obras)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Datos Modificados Correctamente'

    return render(request, 'core/EditarObra.html', datos)

def eliminarObras(request,id):
    Obras= Obra.objects.get(idObra=id)
    Obras.delete()
    return redirect(to="Obras")
