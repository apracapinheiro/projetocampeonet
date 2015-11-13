from django.conf.urls import *
from django.contrib import admin

from django.contrib.auth.views import *
from django.views.generic import TemplateView
from cadastros.views import *
from palpites.views import *
from projetocampeonet import settings
from django.conf.urls.static import static



urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^pontuacao/$', CalculaPontuacao.as_view(), name='pontuacao'),
                       # url(r'^palpite/$', PalpiteView.as_view()),
                       url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
                       url(r'^logout/$', logout_page),
                       url(r'^sucesso/$', sucesso_page, name='sucesso'),
                       
                       url(r'^user/password/reset/$',
                           'django.contrib.auth.views.password_reset',
                           {'post_reset_redirect' : '/user/password/reset/done/'},
                           name="password_reset"),
                       url(r'^user/password/reset/done/$',
                           'django.contrib.auth.views.password_reset_done'),
                       url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           {'post_reset_redirect' : '/user/password/done/'}),
                       url(r'^user/password/done/$',
                           'django.contrib.auth.views.password_reset_complete'),
                       url(r'^galeria/$', TemplateView.as_view(template_name="galeria.html"), name='galeria'), #direciona direto para uma pagina
                       url(r'^', include('palpites.urls')),
                       url(r'^', include('cadastros.urls')),

                       # url(r'^logout/$', 'django.contrib.auth.views.logout'),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
