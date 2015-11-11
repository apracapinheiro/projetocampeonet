from django.conf.urls import url, patterns, include
from django.contrib import admin


from cadastros.views import Criar, register_page, ListaGP, ListaParticipantes
from palpites.views import Index
from django.views.generic import TemplateView



urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^cadastro-participante/$', Criar.as_view(), name='cadastro'),
                       url(r'^register/$', register_page),
                       url(r'^register/success/$', TemplateView.as_view(
                           template_name='registration/register_success.html')),
                       url(r'^lista-gps/$', ListaGP.as_view(), name='listaGP'),
                       url(r'^participantes/$', ListaParticipantes.as_view(), name='participantes'),
                       )

