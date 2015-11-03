# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from cadastros.forms import *
from cadastros.models import *
from palpites.models import *
from palpites.forms import *


class Criar(CreateView):
    template_name = 'cadastro_participante.html'
    model = Participante
    success_url = reverse_lazy('cadastro')
    form = CadastroParticipante



def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register/success/')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = RegistrationForm()
        return render(request, 'registration/register.html', args)
    # print args
    variables = RequestContext(request, {'form': form})

    return render_to_response('registration/register.html', variables)


class ListaGP(ListView):
    template_name = 'lista-gp.html'
    model = CalendarioGP
    # context_object_name = 'lista_gp'

    def get_queryset(self):
        queryset = CalendarioGP.objects.all().order_by('-ativo', '-dataGP')
        return queryset


    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = User.objects.create_user(
    #             username=form.cleaned_data['username'],
    #             password=form.cleaned_data['password1'],
    #             email=form.cleaned_data['email']
    #         )
    #         return HttpResponseRedirect('/')
    # else:
    #     form = RegistrationForm()
    #
    # variables = RequestContext(request, {'form': form})
    #
    # return render_to_response('registration/register.html', variables)


def gerar_pontos(request):
    form = FormGerarPontos()
    return render_to_response(
        'gerar_pontos.html',
        locals(),
        context_instance=RequestContext(request),
    )


class ListaPalpite(ListView):
    template_name = 'lista_palpite.html'
    model = Palpite

    def get_context_data(self, **kwargs):
        context = super(ListaPalpite, self).get_context_data(**kwargs)
        return context


class ListaResultado(ListView):
    template_name = 'resultado_prova.html'
    model = ResultadoProva

    def get_context_data(self, **kwargs):
        context = super(ListaResultado, self).get_context_data(**kwargs)
        return context
