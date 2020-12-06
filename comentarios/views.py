from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comentario
from .serializers import ComentarioSerializer

from publicaciones.serializers import PublicacionSerializer
from publicaciones.models import Publicacion
# Create your views here.
class ComentarioView(viewsets.ModelViewSet):
    
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    @action(methods=(['GET','PATCH','DELETE']), detail=True)
    def publicacion(self, request, pk=None):

        comentario = self.get_object()
        if request.method == 'GET':
            publicacion = comentario.publicacion
            serialized = PublicacionSerializer(publicacion)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        if request.method == 'PATCH':
            publicacion = Publicacion.objects.get(id=request.data['id'])
            serialized = PublicacionSerializer(
                instance=publicacion,
                data=request.data,
                partial=True
            )
            if serialized.is_valid():
                serialized.save()
                return Response(
                    status=status.HTTP_201_CREATED,
                    data=serialized.data
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=serialized.errors
                )

        if request.method == 'DELETE':
            publicacion_id = request.data['id']
            publicacion = Publicacion.objects.get(id=publicacion_id)
            publicacion.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT,
                data=request.data
                )