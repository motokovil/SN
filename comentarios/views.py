from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comentario
from .serializers import ComentarioSerializer
from .pagination import MyPaginationClass

from publicaciones.serializers import PublicacionSerializer
from publicaciones.models import Publicacion
# Create your views here.
class ComentarioView(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    pagination_class = MyPaginationClass

    def get_queryset(self):
        query = {}
        for item in self.request.query_params:
            if item in ['page_size', 'page']:
                continue
            if item in ['publicacion']:
                query[item + '__id'] = self.request.query_params[item]
                continue
            query[item + '__icontains'] = self.request.query_params[item]
        print(query)
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()

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