from livraria.serializers import AutorSerializer
from rest_framework import viewsets
from livraria.models import Autor


class AutorViewSet(viewsets.ModelViewSet):
    '''ViewSet para trazer todos os autores'''
    serializer_class = AutorSerializer
    queryset = Autor.objects.all()
