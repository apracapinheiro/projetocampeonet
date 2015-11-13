# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from projetocampeonet.settings import STATIC_URL

# Create your models here.

CHOICES_TIPO = (
    ('A', 'Administrador'),
    ('U', 'Usuário'),
)

CHOICES_ATIVO =(
    ('0', 'INATIVO'),
    ('1', 'ATIVO'),
)



class Equipe(models.Model):
    nome_equipe = models.CharField(max_length=30, verbose_name='Nome da Equipe')
    ano = models.ForeignKey('Calendario', related_name='id_ano', verbose_name='Ano da Equipe', null=True)

    # id_piloto1 = models.ForeignKey('Piloto', related_name='id_piloto1', verbose_name='Primeiro Piloto')
    # id_piloto2 = models.ForeignKey('Piloto', related_name='id_piloto2', verbose_name='Segundo Piloto')

    def __unicode__(self):
        return self.nome_equipe


class Piloto(models.Model):
    nome_piloto = models.CharField(max_length=30, verbose_name='Nome do Piloto')
    pais = models.CharField(max_length=20, verbose_name='Pais de origem')

    def __unicode__(self):
        return "{0}".format(self.nome_piloto)
        # return self.pais


class EquipePiloto(models.Model):
    id_equipe = models.ForeignKey('Equipe', related_name='id_equipe', verbose_name='Equipe')
    id_piloto1 = models.ForeignKey('Piloto', related_name='id_piloto1', verbose_name='Primeiro Piloto', null=True, blank=True)
    id_piloto2 = models.ForeignKey('Piloto', related_name='id_piloto2', verbose_name='Segundo Piloto', null=True, blank=True)
    ano = models.DateField(verbose_name="Ano da equipe", unique=True, null=True)

    def __unicode__(self):
        return str(self.id_equipe)


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=25, verbose_name='Cidade', unique=True)
    estado = models.CharField(max_length=2, verbose_name='Estado')

    def __str__(self):
        return self.nome_cidade


# class Pessoa(models.Model):
#     class Meta:
#         abstract = True
#
#     nome = models.CharField(max_length=100)
#     data_nascimento = models.DateField()
#     endereco = models.CharField(max_length=100)
#
# class Cliente(Pessoa):
#     compra_sempre = models.BooleanField(default=False)



class Participante(User):
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    telefone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    id_cidade = models.ForeignKey('Cidade', related_name='id_cidade', verbose_name='Cidade')

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    def __unicode__(self):
        # return "{0} - {1}".format(self.first_name, self.last_name)
        return '%s %s' % (self.first_name, self.last_name)
        # return self.first_name


class Calendario(models.Model):
    ano = models.SmallIntegerField(max_length=4, verbose_name='Ano do Calendario da F1', unique=True)

    def __str__(self):
        return str(self.ano)

    class Meta:
        ordering = ('ano',)


class Gp(models.Model):
    nomeGP = models.CharField(max_length=25, verbose_name='Nome do GP')
    pais = models.CharField(max_length=20, verbose_name='Pais do GP')
    bandeira = models.ImageField(verbose_name='Bandeira', max_length=255, blank=True, upload_to='images/')

    def __str__(self):
        return self.nomeGP

    def avatar_image(self):
        return (STATIC_URL + self.bandeira.name) if self.bandeira else None
        # return self.bandeira.name


class CalendarioGP(models.Model):
    id_calendario = models.ForeignKey('Calendario', related_name='id_calendario', verbose_name='Ano')
    id_gp = models.ForeignKey('Gp', related_name='id_gp', verbose_name='Grande Premio')
    dataGP = models.DateField(verbose_name='Data do GP')
    posicao_bonus = models.IntegerField(verbose_name='Posicao bonificada na chegada', blank=True, null=True)
    ativo = models.BooleanField(verbose_name='Ativo/Inativo?', default=None)

    def __unicode__(self):
        # return str(self.id_gp)
        return "{0} - {1}".format(self.id_gp, self.dataGP)

    class Meta:
        ordering = ('dataGP',)