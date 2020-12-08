from django.db import models

# Create your models here.
class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=340)
    
    def __str__(self):
        return self.titulo