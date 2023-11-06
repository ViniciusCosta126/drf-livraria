from livraria.models import models, Autor


class Livro(models.Model):
    '''Model que servira de base para criacao de todos os livros da api'''
    titulo = models.CharField(max_length=255, blank=False, null=False)
    paginas = models.IntegerField()
    thumb = models.ImageField(blank=True)
    ativo = models.BooleanField(default=True)
    sinopse = models.TextField(blank=False, null=False)
    autor = models.ForeignKey(
        "Autor", on_delete=models.CASCADE, related_name='autor')
    categorias = models.ManyToManyField(
        'Categoria', related_name='categorias',)

    def __str__(self):
        return self.titulo
