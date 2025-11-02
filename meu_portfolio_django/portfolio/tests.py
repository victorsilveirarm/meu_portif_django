from django.test import SimpleTestCase
from django.urls import reverse

class PortfolioTests(SimpleTestCase):
    def test_home_url_retorna_200(self):
        """Verifica se a URL da home responde com status 200"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_conteudo_home(self):
        """Verifica se o conteúdo da página contém o texto esperado"""
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Bem-vindo ao meu portfólio")


