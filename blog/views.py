from django.shortcuts import render, redirect
from .models import Libro
from django.utils import timezone

def lista_libros(request):
    libros = Libro.objects.filter(
        fecha_publicacion__lte=timezone.now()
    ).order_by('fecha_publicacion')
    
    return render(request, 'blog/lista_libros.html', {'libros': libros})

def redireccion_evaluacion(request):
    return redirect('evaluacion2')
