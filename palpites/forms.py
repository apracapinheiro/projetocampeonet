__author__ = 'ANDRE PRACA'

from django import forms
from palpites.models import Palpite


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
    # readonly_fields = ('data_palpite',)
    data_palpite = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly':'readonly'})

# somefield = forms.CharField(
#     widget=forms.TextInput(attrs={'readonly':'readonly'})
)

    class Meta:
        model = Palpite


class FormGerarPontos(forms.Form):
    nome = forms.CharField(max_length=50, label=('Nome'))
    email = forms.EmailField(required=False, label=('E-mail'))
    mensagem = forms.Field(
        widget=forms.Textarea, label=('Mensagem')
)