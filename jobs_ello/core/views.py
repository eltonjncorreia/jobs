from django.shortcuts import render
from jobs_ello.core.models import Parlamentar, Mandato, Suplente, Exercicio, PrimeiraLegislatura, SegundaLegislatura
import requests
import json


def home(request):
    salvar_dados()
    todos = Parlamentar.objects.all()
    return render(request, 'core/index.html', {'t': todos})


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


def pegar_suplentes(mandato, chave_suplente, lista_suplente):
    if type(chave_suplente) == list:
        for sup in chave_suplente:
            suplentes = create_suplente(mandato, sup)
            lista_suplente.append(suplentes)

    if type(chave_suplente) == dict:
        suplentes = create_suplente(mandato, chave_suplente)
        lista_suplente.append(suplentes)

    return lista_suplente


def pegar_exercicios(mandato, chave_exercicio,  lista_exercicios):
    if type(chave_exercicio) == list:
        for ex in chave_exercicio:
            exe = create_exercicio(mandato, ex)
            lista_exercicios.append(exe)

    if type(chave_exercicio) == dict:
        exe = create_exercicio(mandato, chave_exercicio)
        lista_exercicios.append(exe)

    return lista_exercicios


def create_parlamentar(chave):
    parlamentar = Parlamentar.objects.create(codigo_do_parlamentar=chave.get('CodigoParlamentar'),
                                             nome_do_parlamentar=chave.get('NomeParlamentar'),
                                             nome_completo_do_parlamentar=chave.get('NomeCompletoParlamentar'),
                                             sexo_parlamentar=chave.get('SexoParlamentar'),
                                             forma_de_tratamento=chave.get('FormaTratamento'),
                                             url_foto_parlamentar=chave.get('UrlFotoParlamentar'),
                                             url_pagina_parlamentar=chave.get('UrlPaginaParlamentar'),
                                             email_parlamentar=chave.get('EmailParlamentar'),
                                             sigla_partido_parlamentar=chave.get('SiglaPartidoParlamentar'),
                                             estado_parlamentar=chave.get('UfParlamentar'))
    return parlamentar


def create_mandato(chave, chave_mandato):
    mandato = Mandato.objects.create(parlamentar=create_parlamentar(chave),
                                     codigo_mandato=chave_mandato.get('CodigoMandato'),
                                     uf_parlamentar=chave_mandato.get('UfParlamentar'),
                                     descricao_participacao=chave_mandato.get('DescricaoParticipacao'))
    return mandato


def create_primeira_legislatura(mandato, chave_primeira_legislatura):
    primeira_legislatura = PrimeiraLegislatura(mandato=mandato,
                                               numero_legislatura=chave_primeira_legislatura.get(
                                                   'NumeroLegislatura'),
                                               data_inicio=chave_primeira_legislatura.get('DataInicio'),
                                               data_fim=chave_primeira_legislatura.get('DataFim'))
    return primeira_legislatura


def create_segunda_legislatura(mandato, chave_segunda_legislatura):
    segunda_legislatura = SegundaLegislatura(mandato=mandato,
                                             numero_legislatura=chave_segunda_legislatura.get('NumeroLegislatura'),
                                             data_inicio=chave_segunda_legislatura.get('DataInicio'),
                                             data_fim=chave_segunda_legislatura.get('DataFim'))
    return segunda_legislatura


def create_suplente(mandato, sup):
    suplente = Suplente(mandato=mandato,
                        codigo_suplente=sup.get('CodigoParlamentar'),
                        descricao_participacao=sup.get('DescricaoParticipacao'),
                        nome_parlamentar=sup.get('NomeParlamentar'))
    return suplente


def create_exercicio(mandato, ex):
    exercicio = Exercicio(mandato=mandato,
                          codigo_exercicio=ex.get('CodigoExercicio'),
                          data_inicio=ex.get('DataInicio'),
                          data_fim=ex.get('DataFim'),
                          sigla_data_afastamento=ex.get('SiglaCausaAfastamento'),
                          causa_afastamento=ex.get('DescricaoCausaAfastamento'),
                          data_leitura=ex.get('DataLeitura'))
    return exercicio
