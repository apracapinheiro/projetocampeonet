from django import forms

import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import CreateView
from cadastros.models import Participante


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=20)
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirmacao senha', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
            username = self.cleaned_data['username']

            if not re.search(r'^\w+$', username):
                raise forms.ValidationError('Login de usuario so pode conter caracteres alfanumericos e underscore_')

            try:
                User.objects.get(username=username)
            except ObjectDoesNotExist:
                return username
            raise forms.ValidationError('login de usuario ja utilizado')

    def clean_password2(self):
            if 'password1' in self.cleaned_data:
                password1 = self.cleaned_data['password1']
                password2 = self.cleaned_data['password2']

                if password1 == password2:
                    return password2

            raise forms.ValidationError('Senhas nao conferem!')

    def save(self, commit=True):
        # user = super(RegistrationForm, self).save(commit=False)
        # user.username = self.cleaned_data['username']
        # user.email = self.cleaned_data['email']
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1'],
            email=self.cleaned_data['email']
        )
        if commit:
            user.save()

        return user

        # def clean_password2(self):
        #     if 'password1' in self.cleaned_data:
        #         password1 = self.cleaned_data['password1']
        #         password2 = self.cleaned_data['password2']
        #
        #         if password1 == password2:
        #             return password2
        #
        #     raise forms.ValidationError('Senhas nao conferem!')
        #
        # def clean_username(self):
        #     username = self.cleaned_data['username']
        #
        #     if not re.search(r'^\w+$', username):
        #         raise forms.ValidationError('Login de usuario so pode conter caracteres alfanumericos e underscore_')
        #
        #         try:
        #             User.objects.get(username=username)
        #         except ObjectDoesNotExist:
        #             return username
        #         raise forms.ValidationError('Login de usuario ja utilizado')


"""
Cadastros de participantes, substituicao do campo senha.
"""


class CadastroParticipante(forms.Form):
    # senha = forms.CharField(max_length=10, widget=forms.PasswordInput())

    class Meta:
        model = Participante
        fields = '__all__'
