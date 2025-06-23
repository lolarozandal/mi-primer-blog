from django.conf import settings
from django.db import models
from django.utils import timezone

class Libro(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    portada = models.ImageField(upload_to='portadas/', blank=True, null=True)
    estrellas = models.IntegerField(default=0)  # Valor de 0 a 5, por ejemplo
    opinion_personal = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.titulo
