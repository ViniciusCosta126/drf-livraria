from livraria.models import models


class Autor(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    nacionalidade = models.CharField(max_length=100)


    def __str__(self):
        return self.nome