from django.test import TestCase
from livraria.models import Autor, Livro, Categoria


class TestModelCaseLivro(TestCase):

    def setUp(self):
        self.autor = Autor(
            nome="Machado de Assis",
            nacionalidade="Brasileiro"
        )
        self.autor.save()

        self.categoria = Categoria(
            nome="Terror"
        )
        self.categoria.save()
        
        self.livro = Livro(
            titulo="Dom Casmurro",
            paginas=208,
            sinopse="Qualquer coisas",
            autor=self.autor,
        )
        self.livro.save()
        self.livro.categorias.add(self.categoria)

    def test_verifica_os_atributos_default_e_instanciamento_de_livro(self):
        '''Verifica se os atributos default estao sendo definidos de forma correta, e os atributos que foram passados estão sendo inseridos de forma correta'''

        self.assertEqual(self.livro.titulo, "Dom Casmurro")
        self.assertEqual(self.livro.paginas, 208)
        self.assertEqual(self.livro.sinopse, "Qualquer coisas")
        self.assertEqual(self.livro.autor.nome, "Machado de Assis")
