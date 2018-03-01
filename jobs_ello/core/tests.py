from django.test import TestCase
from django.shortcuts import resolve_url as r

from jobs_ello.core.views import salvar_dados


class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """GET / return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_json(self):
        self.assertTrue(self.resp, salvar_dados())

    def test_template(self):
        """Esta usando o template core/index.html"""
        self.assertTemplateUsed(self.resp, 'core/index.html')

