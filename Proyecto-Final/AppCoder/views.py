from unicodedata import name
from django import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import PosteoFormulario

#importamos los modelos y forms creados
# Definimos las funciones que se renderizan y conectan con los templates
"""  """

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def campeones(request):
    campeones = Campeon.objects.all()
    return render(context={'campeones': campeones},request=request, template_name='AppCoder/campeones.html')
 
def items(request):
    items = Item.objects.all()
    return render(context={'items': items},request=request, template_name='AppCoder/items.html')

def posteos(request):
    posteos = Posteo.objects.all()
    return render(context={'posteos': posteos},request=request, template_name='AppCoder/posteos.html')

def buscar_campeon(request):
    if request.GET:
        campeones = Campeon.objects.filter(nombre=request.GET.get('nombre')).all() # de los campeones obtener solamente aquellos en los que el nombre que viene en el request (url) sea igual que alguno que tengamos en la base de datos
    return render(context={'campeones': campeones},request=request, template_name='AppCoder/campeones.html')

def formulario_posteo(request):
    form = PosteoFormulario()
    return render(request=request, template_name='AppCoder/insert_post.html', context={'form': form})

#En caso de que venga por Post, recibimos los datos desde el form, los valida y nos los trae limpio con cleaned.data. Guarda los distintos campos en la clase Posteo y los guarda

def insertar_posteo(request):
    if request.method == 'POST':
        form= PosteoFormulario(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            posteo = Posteo(
                    titulo = form['titulo'],
                    cuerpo = form.get('cuerpo'),
                    autor = form['autor'],
                    fecha = form['fecha']
                )
            posteo.save()
            return render(request=request, template_name='AppCoder/posteos.html',context={'posteos': [posteo]})
    return render(request=request, template_name='AppCoder/posteos.html',context={'posteos': []})
