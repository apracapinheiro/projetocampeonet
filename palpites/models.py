from django.db import models
from cadastros.models import Participante, Gp, Piloto



class Palpite(models.Model):
    participante = models.ForeignKey('cadastros.Participante', related_name='id_participante', verbose_name='Participante')
    id_calendarioGP = models.ForeignKey('cadastros.CalendarioGP', related_name='id_palpiteGP', verbose_name='GP', null=True, blank=True)
    data_palpite = models.DateTimeField('Data do palpite', auto_now=True)
    palp_pole = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Pole Position')
    palp_segLarg = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Segundo Largada')
    palp_tercLarg = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Terceiro Largada')
    palp_quaLarg = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Quarto Largada')
    palp_quinLarg = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Quinto Largada')
    palp_vencedor = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Vencedor')
    palp_vegLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Segundo Lugar')
    palp_tercLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Terceiro Lugar')
    palp_quaLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Quarto Lugar')
    palp_quinLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Quinto Lugar')
    palp_sexLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Sexto Lugar')
    palp_setLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Setimo Lugar')
    palp_oitLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Oitavo Lugar')
    palp_nonLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Nono Lugar')
    palp_decLug = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Decimo Lugar')
    palp_volta = models.ForeignKey('cadastros.Piloto', related_name='+', verbose_name='Volta Rapida')
    comentario = models.TextField(max_length=500)

    class Meta:
        ordering = ['participante', 'data_palpite']
        verbose_name = 'Palpite'
        verbose_name_plural = 'Palpites'

    def __unicode__(self):
        return "{0} - {1}".format(self.data_palpite, self.comentario)


class ResultadoProva(models.Model):
    id_calendarioGP = models.ForeignKey('cadastros.CalendarioGP', related_name='id_calendarioGP', verbose_name='Grande Premio', null=True, blank=True)
    polePosition = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Pole Position')
    segundoLargada = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Segundo Largada')
    terceiroLargada = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Terceiro Largada')
    quartoLargada = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Quarto Largada')
    quintoLargada = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Quinto Largada')
    vencedor = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Vencedor')
    segundoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Segundo Lugar')
    terceiroLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Terceiro Lugar')
    quartoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Quarto Lugar')
    quintoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Quinto Lugar')
    sextoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Sexto Lugar')
    setimoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Setimo Lugar')
    oitavoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Oitavo Lugar')
    nonoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Nono Lugar')
    decimoLugar = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Decimo Lugar')
    voltaRapida = models.ForeignKey('cadastros.Piloto', related_name='+',verbose_name='Piloto Volta Rapida')

    class Meta:
        ordering = ['id_calendarioGP']
        verbose_name = 'Resultado do GP'
        verbose_name_plural = 'Resultados dos GPs'

    def __unicode__(self):
        return "{0}".format(self.id_calendarioGP)


class PontoParticipante(models.Model):
    TotalPontos = models.SmallIntegerField(verbose_name='Total de Pontos')
    participante = models.ForeignKey('cadastros.Participante', related_name='+', verbose_name='Participante')


class Pontos(models.Model):
    pole = models.SmallIntegerField(verbose_name='Pontos Pole Position')
    segLarg = models.SmallIntegerField(verbose_name='Pontos Segundo Largada')
    tercLarg = models.SmallIntegerField(verbose_name='Pontos Terceiro Largada')
    quaLarg = models.SmallIntegerField(verbose_name='Pontos Quarto Largada')
    quinLarg = models.SmallIntegerField(verbose_name='Pontos Quinto Largada')
    vencedor = models.SmallIntegerField(verbose_name='Pontos Vencedor')
    vegLug = models.SmallIntegerField(verbose_name='Pontos Segundo Lugar')
    tercLug = models.SmallIntegerField(verbose_name='Pontos Terceiro Lugar')
    quaLug = models.SmallIntegerField(verbose_name='Pontos Quarto Lugar')
    quinLug = models.SmallIntegerField(verbose_name='Pontos Quinto Lugar')
    sexLug = models.SmallIntegerField(verbose_name='Pontos Sexto Lugar')
    setLug = models.SmallIntegerField(verbose_name='Pontos Setimo Lugar')
    oitLug = models.SmallIntegerField(verbose_name='Pontos Oitavo Lugar')
    nonLug = models.SmallIntegerField(verbose_name='Pontos Nono Lugar')
    decLug = models.SmallIntegerField(verbose_name='Pontos Decimo Lugar')
    volta = models.SmallIntegerField(verbose_name='Pontos Volta Rapida')
    bonus = models.SmallIntegerField(verbose_name='Pontos Bonificacao')


class Pontuacao(models.Model):
    id_palpite = models.ForeignKey('Palpite', related_name='id_Palpite', verbose_name='Palpite')
    pole = models.SmallIntegerField(verbose_name='Pontuacao para Pole Position')
    segLarg = models.SmallIntegerField(verbose_name='Pontuacao para Segundo Largada')
    tercLarg = models.SmallIntegerField(verbose_name='Pontuacao para Terceiro Largada')
    quaLarg = models.SmallIntegerField(verbose_name='Pontuacao para Quarto Largada')
    quinLarg = models.SmallIntegerField(verbose_name='Pontuacao para Quinto Largada')
    vencedor = models.SmallIntegerField(verbose_name='Pontuacao para Vencedor')
    segLug = models.SmallIntegerField(verbose_name='Pontuacao para Segundo Lugar')
    tercLug = models.SmallIntegerField(verbose_name='Pontuacao para Terceiro Lugar')
    quaLug = models.SmallIntegerField(verbose_name='Pontuacao para Quarto Lugar')
    quinLug = models.SmallIntegerField(verbose_name='Pontuacao para Quinto Lugar')
    sexLug = models.SmallIntegerField(verbose_name='Pontuacao para Sexto Lugar')
    setLug = models.SmallIntegerField(verbose_name='Pontuacao para Setimo Lugar')
    oitLug = models.SmallIntegerField(verbose_name='Pontuacao para Oitavo Lugar')
    nonLug = models.SmallIntegerField(verbose_name='Pontuacao para Nono Lugar')
    decLug = models.SmallIntegerField(verbose_name='Pontuacao para Decimo Lugar')
    volta = models.SmallIntegerField(verbose_name='Pontuacao para Volta Rapida')
    bonus = models.SmallIntegerField(verbose_name='Pontuacao Bonificada')
    total = models.SmallIntegerField(verbose_name='Pontuacao Total')