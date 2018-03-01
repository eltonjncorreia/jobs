import json

import requests
from django.shortcuts import render

from jobs_ello.core.models import Parlamentar, Suplente, Exercicio
from jobs_ello.core.models import PrimeiraLegislatura, SegundaLegislatura
from jobs_ello.core.negocios import create_mandato, create_primeira_legislatura
from jobs_ello.core.negocios import create_segunda_legislatura, pegar_suplentes, pegar_exercicios


def home(request):
    salvar_dados()
    todos_parlamentares = Parlamentar.objects.all()
    return render(request, 'core/index.html', {'parlamentares': todos_parlamentares})


def buscar_parlamentares():
    response = requests.get('http://legis.senado.gov.br/dadosabertos/senador/lista/atual.json')
    content = json.loads(response.content)
    parlamentares = content['ListaParlamentarEmExercicio'].get('Parlamentares').get('Parlamentar')
    return parlamentares


def salvar_dados():
    lista_primeira_legislacao = []
    lista_segunda_legislacao = []
    lista_suplente = []
    lista_exercicios = []

    for dado in buscar_parlamentares():

        chave = dado['IdentificacaoParlamentar']

        chave_mandato = dado['Mandato']

        mandato = create_mandato(chave, chave_mandato)

        chave_primeira_legislatura = chave_mandato.get('PrimeiraLegislaturaDoMandato')
        primeira_legislacao = create_primeira_legislatura(mandato, chave_primeira_legislatura)
        lista_primeira_legislacao.append(primeira_legislacao)

        chave_segunda_legislatura = chave_mandato.get('SegundaLegislaturaDoMandato')
        segunda_legislacao = create_segunda_legislatura(mandato, chave_segunda_legislatura)
        lista_segunda_legislacao.append(segunda_legislacao)

        chave_suplente = chave_mandato.get('Suplentes').get('Suplente')
        lista_suplente = pegar_suplentes(mandato, chave_suplente, lista_suplente)

        chave_exercicio = chave_mandato.get('Exercicios').get('Exercicio')
        lista_exercicios = pegar_exercicios(mandato, chave_exercicio, lista_exercicios)

    PrimeiraLegislatura.objects.bulk_create(lista_primeira_legislacao)
    SegundaLegislatura.objects.bulk_create(lista_segunda_legislacao)
    Suplente.objects.bulk_create(lista_suplente)
    Exercicio.objects.bulk_create(lista_exercicios)

