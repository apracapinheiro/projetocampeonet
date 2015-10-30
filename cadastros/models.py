# -*- coding: utf-8 -*-

from django.db import models
from django import forms

# Create your models here.

CHOICES_TIPO = (
    ('A', 'Administrador'),
    ('U', 'Usuário'),
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

    def __unicode__(self):
        return str(self.id_equipe)


class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=25, verbose_name='Cidade', unique=True)
    estado = models.CharField(max_length=2, verbose_name='Estado')

    def __str__(self):
        return self.nome_cidade


class Participante(models.Model):
    nome = models.CharField(max_length=50, verbose_name="Nome do participante")
    endereco = models.CharField(max_length=100, verbose_name="Endereço")
    telefone = models.CharField(max_length=15, blank=True, verbose_name="Telefone")
    id_cidade = models.ForeignKey('Cidade', related_name='id_cidade', verbose_name='Cidade')
    email = models.EmailField(max_length=60, unique=True, verbose_name="E-mail")
    tipo = models.CharField(max_length=1, choices=CHOICES_TIPO, verbose_name="Tipo usuário")
    login = models.CharField(max_length=15, unique=True, verbose_name="Login")
    senha = models.CharField(max_length=10, verbose_name="Senha")
    criado_em = models.DateTimeField(auto_now=True, verbose_name="Data criação cadastro")

    class Meta:
        ordering = ['nome']
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'

    def __str__(self):
        return self.nome


class Calendario(models.Model):
    ano = models.SmallIntegerField(max_length=4, verbose_name='Ano do Calendario da F1', unique=True)

    def __str__(self):
        return str(self.ano)

    class Meta:
        ordering = ('ano',)


class Gp(models.Model):
    nomeGP = models.CharField(max_length=25, verbose_name='Nome do GP')
    pais = models.CharField(max_length=20, verbose_name='Pais do GP')
    # anoGP = models.ManyToManyField('Calendario')
    # id_Calendario = models.ForeignKey('Calendario', related_name='id_calendario', null=True, blank=True)

    def __str__(self):
        return self.nomeGP


class CalendarioGP(models.Model):
    id_calendario = models.ForeignKey('Calendario', related_name='id_calendario', verbose_name='Ano')
    id_gp = models.ForeignKey('Gp', related_name='id_gp', verbose_name='Grande Premio')
    dataGP = models.DateField(verbose_name='Data do GP')

    def __unicode__(self):
        # return str(self.id_gp)
        return "{0} - {1}".format(self.id_gp, self.dataGP)

    class Meta:
        ordering = ('dataGP',)