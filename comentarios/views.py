from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comentario
from .serializers import ComentarioSerializer
from publicaciones.serializers import PublicacionSerializer

# Create your views here.
class ComentarioView(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(methods=(['GET']), detail=True)
    def publicacion(self, request, pk=None):
        comentario = self.get_object()
        publicacion = comentario.publicacion
        serialized = PublicacionSerializer(publicacion)

        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )