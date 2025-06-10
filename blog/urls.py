from django.urls import path
from . import views
urlpatterns = [
    path('', views.lista_public, name='lista_public'),  # cuando la URL esté vacía, muestra la lista de posts
]