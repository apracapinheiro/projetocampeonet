# coding=utf-8
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View, CreateView, ListView
from cadastros.models import CalendarioGP
from palpites.forms import CadastroPalpiteForm, PalpiteForm, FormGerarPontos
from forms import FormPalpite
# from palpites.models import Palpite as Lista
from palpites.models import Palpite, ResultadoProva, Pontuacao, Pontos


class PalpiteView(View):
    def get(self, request):
        form = FormPalpite()
        paramns = dict()
        paramns["form"] = form
        return render(request, 'palpite.html', paramns)


class Index(View):
    def get(self, request):
        paramns = {}
        paramns["name"] = "CampeoNET"
        return render(request, 'main_page.html', paramns)

def sucesso_page(request):
    return render_to_response('sucesso.html', context_instance=RequestContext(request))


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


class CadastroPalpite(CreateView):
    template_name = 'cadastro_palpite.html'
    model = Palpite
    success_url = reverse_lazy('cadastro_palpite')
    form = CadastroPalpiteForm
    # fields = '__all__'


# class Palpite(CreateView):
#     template_name = 'cadastro_palpite_old.html'
#     # model = Palpite
#     success_url = reverse_lazy('cadastro_palpite_old')
#     form = PalpiteForm
#     exclude = ['participante',]


class ListaPalpites(ListView):
    template_name = 'lista-palpites-geral.html'
    model = Palpite
    # context_object_name = 'lista_gp'

    def get_queryset(self):
        queryset = Palpite.objects.all().filter(id_calendarioGP__ativo=1)
        return queryset


class ListaPalpiteParticipante(ListView):
    template_name = 'palpite-participante.html'
    model = Palpite

    def get_queryset(self):
        palpite_id = int(self.kwargs['pk'])
        queryset = Palpite.objects.filter(id=palpite_id)
        return queryset


def cria_palpite(request):
    # Formulário enviado
    form = PalpiteForm(request.POST or None, user=request.user, ativo=1)
    if form.is_valid():
        form.save()
        return redirect('sucesso')

    return render(request, "cadastro_palpite_old.html", {'form': form})

@login_required(login_url='/login/')
def CalculaPontuacao(request):

    GP = CalendarioGP.objects.filter(ativo=1).values_list('id', 'posicao_bonus') # busca prova que está com o status ativo

    idGP = GP[0][0] # id do GP ativo
    bonus = GP[0][1] # posicao bonificada da prova
    form = FormGerarPontos()

    resultado = ResultadoProva.objects.filter(id_calendarioGP=idGP).values_list('polePosition', 'segundoLargada',
                                                            'terceiroLargada', 'quartoLargada', 'quintoLargada',
                                                            'vencedor', 'segundoLugar', 'terceiroLugar', 'quartoLugar',
                                                            'quintoLugar', 'sextoLugar', 'setimoLugar', 'oitavoLugar',
                                                             'nonoLugar', 'decimoLugar', 'voltaRapida')

    palpites = Palpite.objects.all().filter(id_calendarioGP=idGP).values_list('palp_pole', 'palp_segLarg',
                                                            'palp_tercLarg', 'palp_quaLarg', 'palp_quinLarg',
                                                            'palp_vencedor', 'palp_vegLug', 'palp_tercLug',
                                                            'palp_quaLug', 'palp_quinLug', 'palp_sexLug', 'palp_setLug',
                                                            'palp_oitLug', 'palp_nonLug', 'palp_decLug', 'palp_volta', 'id')

    pontos = Pontos.objects.all().values_list('pole', 'segLarg', 'tercLarg', 'quaLarg', 'quinLarg',
                                                            'vencedor', 'vegLug', 'tercLug',
                                                            'quaLug', 'quinLug', 'sexLug', 'setLug',
                                                            'oitLug', 'nonLug', 'decLug', 'volta', 'bonus')

    pontuacao = []

    for listapalpites in palpites:
        count = 0
        total = 0
        for item in listapalpites:
            if count < 16:
                if item == resultado[0][count]:
                    pontuacao.insert(count, pontos[0][count])
                    total = total + pontos[0][count]
                    if bonus == count-4: # se a posicao bonificada tiver acerto no palpite, é feito o somatorio
                        total = total + pontos[0][16] # a pontuacao do bonus é a ultima posicao do objeto pontos
                else:
                    pontuacao.insert(count, '0')
                count += 1
            else:
                count = 0

        id_palpite_participante = Palpite.objects.get(id=listapalpites[16]) #cria objeto palpite para poder inserir o id na tabela pontuacao

        pontos_participante = Pontuacao.objects.create(id_palpite=id_palpite_participante,
                                                       pole=pontuacao[0],
                                                       segLarg=pontuacao[1],
                                                       tercLarg=pontuacao[2],
                                                       quaLarg=pontuacao[3],
                                                       quinLarg=pontuacao[4],
                                                       vencedor=pontuacao[5],
                                                       segLug=pontuacao[6],
                                                       tercLug=pontuacao[7],
                                                       quaLug=pontuacao[8],
                                                       quinLug=pontuacao[9],
                                                       sexLug=pontuacao[10],
                                                       setLug=pontuacao[11],
                                                       oitLug=pontuacao[12],
                                                       nonLug=pontuacao[13],
                                                       decLug=pontuacao[14],
                                                       volta=pontuacao[15],
                                                       bonus=bonus,
                                                       total=total
                                                       )
        pontos_participante.save()

        # print pontuacao

        pontuacao = []

    return render(request, 'pontos.html')



# def gerar_pontos(request):
#     form = FormGerarPontos()
#     return render_to_response(
#         'gerar_pontos.html',
#         locals(),
#         context_instance=RequestContext(request),
#     )


# def consulta(request, pk):#pk = nome da quadra
#
#     pk = (" ").join(pk.split("-"))
#     quadra = Localidade.objects.filter(nome_localidade=pk)
#     for qd in quadra:
#         pk2 = qd.id
#         nome_quadra = qd.nome_localidade
#
#     enderecos = Imovel.objects.filter(cod_localidade_id=pk2)  # acessa imoveis pelo cod da localidade
#     soma_habitantes = 0
#     soma_cachorro = 0
#     soma_gato = 0
#     soma_roedores = Imovel.objects.filter(cod_localidade_id=pk2, roedores="s").count()
#     soma_esquito = 0 #esquitossomose nao tem dados salvo no banco ainda
#     soma_poco = 0
#     soma_caixa = 0
#     soma_malaria = 0 #nao tem dados salvo no banco ainda
#     soma_dengue = 0 #nao tem dados salvo no banco ainda
#     soma_leish = 0 #nao tem dados salvo no banco ainda
#     soma_malucosa = 0 #Nao tem dados salvos no banco ainda
#     soma_peste = 0 #nao tem dados salvo no banco ainda
#     soma_chagas = 0 #nao tem dados salvo no banco ainda
#     soma_febre_amarela = 0 #nao tem dados salvo no banco ainda
#     soma_residencia = Imovel.objects.filter(cod_localidade_id=pk2, tipo_imovel="RES").count()
#     soma_comercio = Imovel.objects.filter(cod_localidade_id=pk2, tipo_imovel="COM").count()
#     soma_outros = Imovel.objects.filter(cod_localidade_id=pk2, tipo_imovel="OUT").count()
#     soma_pontos_estrategicos = Imovel.objects.filter(cod_localidade_id=pk2, tipo_imovel="PE").count()
#     soma_armadilha = 0 #nao tem dados salvo no banco ainda
#     soma_terreno_baldio = Imovel.objects.filter(cod_localidade_id=pk2, tipo_imovel="TB").count()
#     lista_quarteiroes = []
#     data_cadastro = date.today()
#     for endereco in enderecos:
#         soma_habitantes = soma_habitantes + int(endereco.habitantes_qtde)
#         soma_cachorro = soma_cachorro + int(endereco.cachorro_qtde)
#         soma_gato = soma_gato + int(endereco.gato_qtde)
#         soma_poco = soma_poco + int(endereco.poco_qtde)
#         soma_caixa = soma_caixa + int(endereco.cx_dagua_qtde)
#         lista_quarteiroes.append(endereco.num_quarteirao)
#     soma_quarteiroes = tira_repetido_quarteiroes(lista_quarteiroes)
#     mensagem = {}
#     if request.method == 'POST':
#         #print "entrei em POST"
#
#         if checa_redundancia(data_cadastro,soma_cachorro,soma_gato,soma_roedores,soma_malaria,soma_dengue,soma_esquito,
#                             soma_leish,soma_malucosa, soma_peste,soma_chagas,soma_febre_amarela, soma_residencia,
#                             soma_comercio,soma_outros,soma_habitantes,soma_quarteiroes,soma_pontos_estrategicos, soma_armadilha,
#                             soma_terreno_baldio,pk2):
#             mensagem['msg'] = u"A quadra %s foi salva no histórico com sucesso!!!"%nome_quadra
#             form = LocalidadeHistorico(data_atualizacao=data_cadastro, cachorro_qtde=soma_cachorro,
#                                            gato_qtde=soma_gato, roedores_qtde=soma_roedores, malaria_qtde = soma_malaria,
#                                            dengue_qtde = soma_dengue,esquisto_qtde = soma_esquito,leish_qtde = soma_leish,
#                                            malucosa_qtde = soma_malucosa, peste_qtde = soma_peste,chagas = soma_chagas,
#                                            amarela = soma_febre_amarela, residencia_qtde = soma_residencia,
#                                            comercio_qtde = soma_comercio, outros_qtde = soma_outros,
#                                            habitantes_qtde = soma_habitantes, quarteiroes = soma_quarteiroes,
#                                            pe_qtde = soma_pontos_estrategicos, armadilha_qtde = soma_armadilha,
#                                            ter_baldios_qtde = soma_terreno_baldio,
#                                            localidade_id = pk2)
#             form.save()
#         else:
#
#             mensagem['msg'] = u"Esses dados da quadra %s já estão salvo no sistema!!!"%nome_quadra
#
#
#
#     return render(request, 'exibir_qtda.html', {
#         'soma_habitantes': soma_habitantes, 'soma_cachorros': soma_cachorro,"soma_roedores":soma_roedores,
#         "soma_gato": soma_gato,"soma_poco": soma_poco, "soma_caixa": soma_caixa, "quadra": nome_quadra,
#         "soma_residencia": soma_residencia,"soma_comercio": soma_comercio, "soma_malaria": soma_malaria,
#         "soma_dengue": soma_dengue, "soma_leish": soma_leish,"soma_malucosa": soma_malucosa, "soma_peste": soma_peste,
#         "soma_chagas": soma_chagas, "soma_febre_amarela": soma_febre_amarela, "soma_outros": soma_outros,
#         "soma_quarteiroes": soma_quarteiroes, "soma_pontos_estrategicos": soma_pontos_estrategicos,
#         "soma_amardilha": soma_armadilha,"soma_terreno_baldio": soma_terreno_baldio,"soma_esquito":soma_esquito,
#         "mensagem_salva":mensagem
#
#     })