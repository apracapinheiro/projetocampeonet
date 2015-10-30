from django.contrib import admin
from palpites.models import Palpite, ResultadoProva, PontoParticipante, Pontos, Pontuacao


class PalpiteAdmin(admin.ModelAdmin):
    list_display = ('participante', 'id_calendarioGP')


class ResultadoProvaAdmin(admin.ModelAdmin):
    list_display = ('id_calendarioGP', 'polePosition')


class PontoParticipanteAdmin(admin.ModelAdmin):
    list_display = ('TotalPontos', 'participante')


# class PontosAdmin(admin.ModelAdmin):
#     list_display = ('')


class PontuacaoAdmin(admin.ModelAdmin):
    list_display = ('id_palpite', 'pole')


# class GpInLine(admin.TabularInline):
#     model = Gp
#     extra = 10
#
#
# class CalendarioAdmin(admin.ModelAdmin):
#     # model = Calendario
#     list_display = ('ano', 'id')
#     inlines = [GpInLine]


# Register your models here.

admin.site.register(Palpite, PalpiteAdmin)
admin.site.register(ResultadoProva, ResultadoProvaAdmin)
admin.site.register(PontoParticipante, PontoParticipanteAdmin)
admin.site.register(Pontuacao, PontuacaoAdmin)

