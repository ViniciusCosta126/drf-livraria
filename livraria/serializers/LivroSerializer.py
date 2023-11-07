from rest_framework import serializers
from livraria.serializers import CategoriaSerializer
from livraria.models import Livro


class LivroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livro
        fields = '__all__'
