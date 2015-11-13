from django.contrib import admin
from cadastros.models import Piloto, Equipe, Participante, Cidade, Gp, Calendario, CalendarioGP, EquipePiloto
from projetocampeonet import settings


class ParticipanteAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'username',
        'is_staff',
    )


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome_cidade', 'estado')


class GpAdmin(admin.ModelAdmin):
    list_display = ('nomeGP', 'pais', 'bandeira')


class GpInLine(admin.TabularInline):
    model = Gp
    extra = 10


class CalendarioGPInLine(admin.TabularInline):
    model = CalendarioGP
    extra = 2


class CalendarioAdmin(admin.ModelAdmin):
    model = Calendario
    # list_display = ('ano', 'id')
    inlines = [CalendarioGPInLine]


class CalendarioGPAdmin(admin.ModelAdmin):
    #model = CalendarioGP
    list_display = ('id_calendario', 'dataGP')


# class EquipePilotoInLine(admin.TabularInline):
#     model = EquipePiloto
#     extra = 1


class EquipeAdmin(admin.ModelAdmin):
    model = Equipe
    list_display = ('nome_equipe', 'ano')

    # class Media:
    #     js = (settings.STATIC_URL + 'js/esconde-sinal.js',)
    # inlines = [EquipePilotoInLine]


class PilotoAdmin(admin.ModelAdmin):
    list_display = ('nome_piloto', 'pais')


class EquipePilotoAdmin(admin.ModelAdmin):
    list_display =('id_equipe', 'id_piloto1', 'id_piloto2', 'ano')





# Register your models here.

admin.site.register(Piloto, PilotoAdmin)
admin.site.register(Equipe, EquipeAdmin)
admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Gp, GpAdmin)
admin.site.register(Calendario, CalendarioAdmin)
# admin.site.register(CalendarioGP, CalendarioGPAdmin)
admin.site.register(EquipePiloto, EquipePilotoAdmin)