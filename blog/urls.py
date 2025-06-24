from django.urls import path
from blog import views  # Asegurate de importar tus vistas

urlpatterns = [
    path('', views.redireccion_evaluacion),  # Redirige / a /evaluacion2/
    path('evaluacion2/', views.lista_libros, name='lista_libros'),
]
