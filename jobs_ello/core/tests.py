from django.test import TestCase
from django.shortcuts import resolve_url as r

from jobs_ello.core.views import salvar_dados, buscar_parlamentares


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET / return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Esta usando o template core/index.html"""
        self.assertTemplateUsed(self.resp, 'core/index.html')

    def test_existe_funcao_salvar_dados(self):
        """testa se existe uma funcao chamanda salvar dados"""
        self.assertTrue(self.resp, salvar_dados)

    def test_existe_funcao_buscar_parlamentar(self):
        """se existir uma funcao buscar parlamentares"""
        self.assertTrue(self.resp, buscar_parlamentares)



