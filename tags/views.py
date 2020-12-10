from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Tag
from .serializers import TagSerializer
from .pagination import MyPaginationClass

from publicaciones.models import Publicacion
from publicaciones.serializers import PublicacionSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = MyPaginationClass

    def get_queryset(self):
        query ={}
        for item in self.request.query_params:
            if item in ['page_size','page']:
                continue
            if item in ['publicaciones']:
                query[item+'__id'] = self.request.query_params[item]
                continue
            query[item+'__icontains'] = self.request.query_params[item]           
        self.queryset = self.queryset.filter(**query)
        return super().get_queryset()
    @action(methods=(['GET','POST','DELETE']), detail=True)
    def publicaciones(self,request,pk=None):

        tag = self.get_object()
        if request.method == 'GET':
            serialized = PublicacionSerializer(tag.publicaciones, many=True)
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        if request.method == 'POST':
            serialized = PublicacionSerializer(data=request.data)
            if serialized.is_valid():
                serialized.save()
                tag.publicaciones.add(serialized.data['id'])
                return Response(
                    status=status.HTTP_200_OK,
                    data=serialized.data
                )
        if request.method == 'DELETE':
            publicacion_id = request.data['id']
            publicacion = Publicacion.objects.get(id=publicacion_id)
            publicacion.delete()
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )

