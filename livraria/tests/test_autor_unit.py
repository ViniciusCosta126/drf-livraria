from django.test import TestCase
from livraria.models import Autor


class TestModelAutor(TestCase):

    def setUp(self):
        self.autor = Autor(
            nome="Machado de Assis",
            nacionalidade="Brasileiro"
        )

    def test_verifica_os_atributos_default_e_instanciamento_de_autor(self):
        '''Verifica se os atributos default estao sendo definidos de forma correta, e os atributos que foram passados estão sendo inseridos de forma correta'''

        self.assertEqual(self.autor.nome, 'Machado de Assis')
        self.assertEqual(self.autor.nacionalidade, "Brasileiro")
