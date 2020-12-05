from django.db import models
from publicaciones.models import Publicacion

# Create your models here.
class Tag(models.Model):
    nombre = models.CharField(max_length=200)
    publicaciones = models.ManyToManyField(Publicacion, related_name='tags')

    def __str__(self):
        return self.nombre