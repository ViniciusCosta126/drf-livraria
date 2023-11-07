from livraria.models import Livro
from livraria.serializers import LivroSerializer
from rest_framework import viewsets


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer