from django import template
from cadastros.models import CalendarioGP, Participante
from palpites.models import Palpite, Pontuacao

register = template.Library()


# @register.filter(name='busca_resultado')
# def busca_resultado(calendario_id, args):
#     total_pontos = 'Nenhum'
#     obj_calendario = CalendarioGP.objects.filter(id=calendario_id).first()
#     if obj_calendario:
#         palpite = Palpite.objects.filter(id_calendarioGP=obj_calendario).first()
#         if palpite:
#             pontuacao = Pontuacao.objects.filter(id_palpite=palpite).first()
#             if pontuacao:
#                 total_pontos = pontuacao.total
#     return total_pontos


@register.assignment_tag
def busca_resultado(calendario_id, participante_id):
    total_pontos = '0'
    obj_calendario = CalendarioGP.objects.filter(id=calendario_id).first()
    obj_participante = Participante.objects.filter(id=participante_id).first()
    if obj_calendario and obj_participante:
        palpite = Palpite.objects.filter(id_calendarioGP=obj_calendario, participante=obj_participante).first()
        if palpite:
            pontuacao = Pontuacao.objects.filter(id_palpite=palpite).first()
            if pontuacao:
                total_pontos = pontuacao.total
    return total_pontos