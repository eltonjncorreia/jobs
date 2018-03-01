from django.contrib import admin
from jobs_ello.core.models import Parlamentar, Mandato, Suplente, Exercicio, PrimeiraLegislatura, SegundaLegislatura


class MandatoInline(admin.TabularInline):
    model = Mandato
    extra = 1


class PrimeiraInline(admin.TabularInline):
    model = PrimeiraLegislatura
    extra = 1


class SegundaInline(admin.TabularInline):
    model = SegundaLegislatura
    extra = 1


class SuplenteInline(admin.TabularInline):
    model = Suplente
    extra = 1


class ExercicioInline(admin.TabularInline):
    model = Exercicio
    extra = 1


class MandatoAdminModel(admin.ModelAdmin):
    inlines = [PrimeiraInline] + [SegundaInline] + [SuplenteInline] + [ExercicioInline]
    list_display = ('parlamentar', 'codigo_mandato', 'uf_parlamentar', 'descricao_participacao')


class ParlamentarAdminModel(admin.ModelAdmin):
    inlines = [MandatoInline]
    list_display = ('nome_do_parlamentar', 'codigo_do_parlamentar', 'sigla_partido_parlamentar')


admin.site.register(Parlamentar, ParlamentarAdminModel)
admin.site.register(Mandato, MandatoAdminModel)