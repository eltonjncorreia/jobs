from django.db import models


class Parlamentar(models.Model):
    codigo_do_parlamentar = models.IntegerField('Codigo Parlamentar', blank=True, null=True)
    nome_do_parlamentar = models.CharField('Nome do parlamentar', max_length=100, blank=True, null=True)
    nome_completo_do_parlamentar = models.CharField('Nome Completo', max_length=255, blank=True, null=True)
    sexo_parlamentar = models.CharField('Sexo', max_length=10, blank=True, null=True)
    forma_de_tratamento = models.CharField('Forma de Tratar', max_length=50, blank=True, null=True)
    url_foto_parlamentar = models.URLField('Url da foto', blank=True, null=True)
    url_pagina_parlamentar = models.URLField('Url da Pagina/Site', blank=True, null=True)
    email_parlamentar = models.EmailField('Email', max_length=255, blank=True, null=True)
    sigla_partido_parlamentar = models.CharField('Sigla partido', max_length=10, blank=True, null=True)
    estado_parlamentar = models.CharField('Estado', max_length=2, blank=True, null=True)

    class Meta:
        verbose_name = "Parlamentar"
        verbose_name_plural = "Parlamentares"

    def __str__(self):
        return self.nome_do_parlamentar


class Mandato(models.Model):
    parlamentar = models.ForeignKey('Parlamentar', on_delete=models.CASCADE, related_name='mandatos', blank=True, null=True)
    codigo_mandato = models.IntegerField('Codigo Mandato', blank=True, null=True)
    uf_parlamentar = models.CharField('Estado', max_length=2, blank=True, null=True)
    descricao_participacao = models.CharField('Descricao participacao', max_length=255, blank=True, null=True)

    def __str__(self):
        return self.descricao_participacao


class PrimeiraLegislatura(models.Model):
    mandato = models.ForeignKey('Mandato', on_delete=models.CASCADE, related_name='primeiras', blank=True, null=True)
    numero_legislatura = models.IntegerField('Codigo legislatura', blank=True, null=True)
    data_inicio = models.DateField('Data Inicio', blank=True, null=True)
    data_fim = models.DateField('Data Fim', blank=True, null=True)

    def __str__(self):
        return str(self.mandato)


class SegundaLegislatura(models.Model):
    mandato = models.ForeignKey('Mandato', on_delete=models.CASCADE, related_name='segundas', blank=True, null=True)
    numero_legislatura = models.IntegerField('Codigo legislatura', blank=True, null=True)
    data_inicio = models.DateField('Data Inicio', blank=True, null=True)
    data_fim = models.DateField('Data Fim', blank=True, null=True)

    def __str__(self):
        return str(self.mandato)


class Suplente(models.Model):
    mandato = models.ForeignKey('Mandato', on_delete=models.CASCADE, related_name='suplentes', blank=True, null=True)
    descricao_participacao = models.CharField('Participação', max_length=100, blank=True, null=True)
    codigo_suplente = models.IntegerField('codigo parlamentar', blank=True, null=True)
    nome_parlamentar = models.CharField('Nome', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.descricao_participacao)


class Exercicio(models.Model):
    mandato = models.ForeignKey('Mandato', on_delete=models.CASCADE, related_name='exercicios', blank=True, null=True)
    codigo_exercicio = models.IntegerField('Cogigo exercicio', blank=True, null=True)
    sigla_data_afastamento = models.CharField('Sigla', max_length=5, blank=True, null=True)
    causa_afastamento = models.CharField('Causa ', max_length=255, blank=True, null=True)
    data_inicio = models.DateField('Data inicio', blank=True, null=True)
    data_fim = models.DateField('Data Fim', blank=True, null=True)
    data_leitura = models.DateField('Data Leitura', blank=True, null=True)

    def __str__(self):
        return str(self.codigo_exercicio)
