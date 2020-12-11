from rest_framework.test import APITestCase
from .models import Comentario
from publicaciones.models import Publicacion
from tags.models import Tag
# Create your tests here.

class FiltrarComentarios(APITestCase):

    def setUp(self):
        self.url = 'http://127.0.0.1:8000/'
        self.publicacion = Publicacion.objects.create(
            titulo='Test',
            descripcion='Test'
        )
        self.comentario = Comentario.objects.create(
            contenido='Test',
            publicacion= self.publicacion
        )
        self.tag = Tag.objects.create(nombre='Test')
        self.publicacion.tags.add(self.tag)

    def test_filter(self):
        query = f'contenido={self.comentario.contenido}'
        response = self.client.get(
            f'{self.url}comentarios/?{query}'
        )
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data['results'][0]['contenido'],self.comentario.contenido)
        self.assertEqual(response.data['count'], 1)
        self.assertIsInstance(self.publicacion, Publicacion)