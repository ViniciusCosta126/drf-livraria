from livraria.serializers import CategoriaSerializer
from livraria.models import Categoria
from rest_framework import viewsets


class CategoriaViewSet(viewsets.ModelViewSet):
    '''ViewSet para model de Categorias'''
    queryset = Categoria.objects.filter(ativo=True)
    serializer_class = CategoriaSerializer
