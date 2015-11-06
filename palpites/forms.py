

import user
from cadastros.models import CalendarioGP
from django import forms
from palpites.models import Palpite
from cadastros.models import *


class FormPalpite(forms.Form):
    comentario = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 1, 'cols': 85,
               'placeholder': 'Digite seu comentario aqui'}),
        max_length=250)
    # class Meta:
    #     model = Palpite
    #
    # def __init__(self, *args, **kwargs):
    #     super(FormPalpite, self).__init__(self, *args, **kwargs)


class CadastroPalpiteForm(forms.ModelForm):
    # participante = forms.CharField(label='participante')
    id_calendarioGP = forms.ModelChoiceField(label='GP Atual', queryset=CalendarioGP.objects.all().order_by('-ativo', '-dataGP'))
    # data_palpite = forms.DateTimeField(label='Data do palpite')

    class Meta:
        model = Palpite
        # fields = ('participante', 'data_palpite',)
        exclude = ['participante']


class PalpiteForm(forms.ModelForm):
    query_pilotos = Piloto.objects.all()
    # usuario = User.

    # participante = forms.ChoiceField(label='Participante')
    # participante = forms.ModelChoiceField(label='Participante', queryset=Participante.objects.all())
    participante = forms.ModelChoiceField(label='Participante', queryset=Participante.objects)
    id_calendarioGP = forms.ModelChoiceField(label='GP Atual', queryset=CalendarioGP.objects)
    data_palpite = forms.DateTimeField(label='Data do palpite', widget=forms.DateTimeInput())
    palp_pole = forms.ModelChoiceField(label='Pole Position', queryset=query_pilotos)
    palp_segLarg = forms.ModelChoiceField(label='Segundo largada', queryset=query_pilotos)
    palp_tercLarg = forms.ModelChoiceField(label='Terceiro largada', queryset=query_pilotos)
    palp_quaLarg = forms.ModelChoiceField(label='Quarto largada', queryset=query_pilotos)
    palp_quinLarg = forms.ModelChoiceField(label='Quinto largada', queryset=query_pilotos)
    palp_vencedor = forms.ModelChoiceField(label='Vencedor', queryset=query_pilotos)
    palp_vegLug = forms.ModelChoiceField(label='Segundo colocado', queryset=query_pilotos)
    palp_tercLug = forms.ModelChoiceField(label='Terceiro colocado', queryset=query_pilotos)
    palp_quaLug = forms.ModelChoiceField(label='Quarto colocado', queryset=query_pilotos)
    palp_quinLug = forms.ModelChoiceField(label='Quinto colocado', queryset=query_pilotos)
    palp_sexLug = forms.ModelChoiceField(label='Sexto colocado', queryset=query_pilotos)
    palp_setLug = forms.ModelChoiceField(label='Setimo colocado', queryset=query_pilotos)
    palp_oitLug = forms.ModelChoiceField(label='Oitavo colocado', queryset=query_pilotos)
    palp_nonLug = forms.ModelChoiceField(label='Nono colocado', queryset=query_pilotos)
    palp_decLug = forms.ModelChoiceField(label='Decimo colocado', queryset=query_pilotos)
    palp_volta = forms.ModelChoiceField(label='Volta rapida', queryset=query_pilotos)
    comentario = forms.CharField(label='Comentario', max_length=500, widget=forms.Textarea())
    # participante = forms.CharField(label='Participante')#, widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # data_palpite = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # id_cidade = forms.ModelChoiceField(label='Cidade', queryset=Cidade.objects.all())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.id_calendarioGP = kwargs.pop('ativo', None)
        super(PalpiteForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['participante'].queryset = Participante.objects.filter(id=self.user.id) #filtra o combo participante, com o usuario logado
            self.fields['participante'].initial = self.user # coloca o valor inicial do combo com o valor do usuario logado

        if self.id_calendarioGP:
            self.fields['id_calendarioGP'].queryset = CalendarioGP.objects.filter(ativo=1)
            self.fields['id_calendarioGP'].initial = self.id_calendarioGP

    def clean(self):
        cleaned_data = super(PalpiteForm, self).clean()
        participante = self.cleaned_data.get('participante')
        id_calendarioGP = self.cleaned_data.get('id_calendarioGP')
        data_palpite = self.cleaned_data.get('data_palpite')
        palp_pole = self.cleaned_data.get('palp_pole')

        return self.cleaned_data

    class Meta:
        model = Palpite


    # def __init__(self, *args, **kwargs):
    #     super(CadastroPalpiteForm, self).__init__(self, *args, **kwargs)
    #
    # def save(self, commit=True):
    #     # user = super(RegistrationForm, self).save(commit=False)
    #     # user.username = self.cleaned_data['username']
    #     # user.email = self.cleaned_data['email']
    #     palpite = Palpite.objects.create(
    #         username=self.cleaned_data['username'],
    #         password=self.cleaned_data['password1'],
    #         email=self.cleaned_data['email'],
    #         first_name=self.cleaned_data['first_name'],
    #         last_name=self.cleaned_data['last_name'],
    #         endereco=self.cleaned_data['endereco'],
    #         id_cidade=self.cleaned_data['id_cidade'],
    #         telefone=self.cleaned_data['telefone']
    #     )
    #     if commit:
    #         palpite.save()
    #
    #     return palpite


class FormGerarPontos(forms.Form):
    nome = forms.CharField(max_length=50, label=('Nome'))
    email = forms.EmailField(required=False, label=('E-mail'))
    mensagem = forms.Field(
        widget=forms.Textarea, label=('Mensagem')
)