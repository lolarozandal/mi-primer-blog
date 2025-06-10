from django.shortcuts import render
from .models import Publicacion
from django.utils import timezone


def lista_public(request):
    publicaciones=Publicacion.objects.filter(fecha_creacion=timezone.now()).order_by('fecha_creacion')
    return render(request, 'blog/lista_public.html', {'publicaciones': publicaciones})
 
from django.shortcuts import render
from .models import Publicacion

def blog(request):
    publicaciones = Publicacion.objects.all()  # o con filtros
    return render(request, 'blog/blog.html', {'publicaciones': publicaciones})
