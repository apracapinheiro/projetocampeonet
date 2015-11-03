from django.conf.urls import *
from cadastros.views import *
from palpites.views import *



urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name='index'),
                       url(r'^palpite/$', CadastroPalpite.as_view(), name='cadastro_palpite'),
                       url(r'^lista-palpite/$', ListaPalpite.as_view(), name='lista_palpite'),
                       url(r'^resultado-prova/$', ListaResultado.as_view(), name='resultado_prova'),
                       url(r'^palpites-geral/$', ListaPalpites.as_view(), name='palpites-geral'),
                       # url(r'^pontuacao/$', CalculaPontuacao.as_view(), name='pontuacao'),
                       # url(r'^palpite/$', PalpiteView.as_view()),
                       # url(r'^gerar_pontos/$', 'projetocampeonet.cadastros.views.gerar_pontos', {}, name='gerar_pontos'),
                       # url(r'^gerar_pontos/$', 'cadastros.views.gerar_pontos', {}, name='gerar_pontos'),
                       )
