from django.conf.urls import *
from cadastros.views import *
from palpites.views import *



urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name='index'),
                       url(r'^palpite/$', CadastroPalpite.as_view(), name='cadastro_palpite'),
                       # url(r'^create-supervisor/$', 'TasksManager.views.create_supervisor', name="create_supervisor"),
                       url(r'^palpite2/$', 'palpites.views.cria_palpite', name='cadastro_palpite2'),
                       # url(r'^palpite2/$', Palpite.as_view(), name='cadastro_palpite2'),
                       url(r'^lista-palpite/$', ListaPalpite.as_view(), name='lista_palpite'),
                       url(r'^resultado-prova/$', ListaResultado.as_view(), name='resultado_prova'),
                       url(r'^palpites-geral/$', ListaPalpites.as_view(), name='palpites-geral'),
                       url(r'^palpite-participante/(?P<pk>\d+)$', ListaPalpiteParticipante.as_view(), name='palpite-participante'),

                       # url(r'^pontuacao/$', CalculaPontuacao.as_view(), name='pontuacao'),
                       # url(r'^palpite/$', PalpiteView.as_view()),
                       # url(r'^gerar_pontos/$', 'projetocampeonet.cadastros.views.gerar_pontos', {}, name='gerar_pontos'),
                       # url(r'^gerar_pontos/$', 'cadastros.views.gerar_pontos', {}, name='gerar_pontos'),
                       )
