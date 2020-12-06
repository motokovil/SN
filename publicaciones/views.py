
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Publicacion
from .serializers import PublicacionSerializer

from comentarios.serializers import ComentarioSerializer
from tags.serializers import TagSerializer

from comentarios.models import Comentario
# Create your views here.

class PublicacionView(viewsets.ModelViewSet):
    queryset = Publicacion.objects.all()
    serializer_class = PublicacionSerializer
    
    @action(methods=(['GET','POST','DELETE','PATCH']), detail=True)
    def comentarios(self,request,pk):

        publicacion = self.get_object()
        if request.method == 'GET':
            comentarios = Comentario.objects.filter(publicacion=publicacion)
            serialized = ComentarioSerializer(comentarios, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )

        if request.method == 'POST':
            comentario = {
                "contenido": request.data['contenido'],
                "publicacion": publicacion.id
            }
            serialized = ComentarioSerializer(data=comentario)
            if serialized.is_valid():
                serialized.save()
                return Response(
                    status=status.HTTP_200_OK,
                    data=serialized.data
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=serialized.errors
                )

        if request.method == 'DELETE':
            comentario_id = request.data['id']
            print(comentario_id)
            comentario = Comentario.objects.get(id=int(comentario_id))
            comentario.delete()
            return Response(
                    status=status.HTTP_204_NO_CONTENT
                )
        if request.method == 'PATCH':
            comentario_id = request.data['id']
            comentario = Comentario.objects.get(id=comentario_id)
            serialized = ComentarioSerializer(
                instance=comentario,
                data=request.data
            )
            if serialized.is_valid():
                serialized.save()
                return Response(
                    status=status.HTTP_202_ACCEPTED,
                    data=serialized.data
                )
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    data=serialized.errors
                )



