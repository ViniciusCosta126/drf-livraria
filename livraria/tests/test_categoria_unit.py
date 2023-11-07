from django.test import TestCase
from livraria.models import Categoria


class TestCategoriaModelTestCase(TestCase):

    def setUp(self):
        self.categoria = Categoria(
            nome="Terror"
        )

    def test_verifica_os_atributos_default_e_instanciamento_de_categoria(self):
        '''Verifica se os atributos default estao sendo definidos de forma correta, e os atributos que foram passados estão sendo inseridos de forma correta'''

        self.assertEqual(self.categoria.nome, 'Terror')
        self.assertEqual(self.categoria.ativo, True)
