from django.db import models
from publicaciones.models import Publicacion
# Create your models here.
class Comentario(models.Model):
    contenido = models.CharField(max_length=200)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.contenido