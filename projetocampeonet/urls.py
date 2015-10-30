from django.conf.urls import *
from django.contrib import admin

from django.contrib.auth.views import *
from cadastros.views import *
from palpites.views import *




urlpatterns = patterns('',
                       url(r'^$', Index.as_view(), name='index'),
                       url(r'^admin/', include(admin.site.urls)),
                       # url(r'^pontuacao/$', CalculaPontuacao.as_view(), name='pontuacao'),
                       # url(r'^palpite/$', PalpiteView.as_view()),
                       url(r'^login/$', 'django.contrib.auth.views.login'),
                       url(r'^logout/$', logout_page),
                       
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
                       url(r'^', include('palpites.urls')),
                       url(r'^', include('cadastros.urls')),
                       # url(r'^logout/$', 'django.contrib.auth.views.logout'),
)







# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'projetocampeonet.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^$', Index.as_view()),
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^palpite/$', PalpiteView.as_view()),
#     url(r'^login/$', 'django.contrib.auth.views.login'),
#     url(r'^logout/$', logout_page),
#     url(r'^register/$', register_page),
#     url(r'^register/success/$', TemplateView.as_view(
#         template_name='registration/register_success.html')),
#     url(r'^user/password/reset/$',
#         'django.contrib.auth.views.password_reset',
#         {'post_reset_redirect' : '/user/password/reset/done/'},
#         name="password_reset"),
#     url(r'^user/password/reset/done/$',
#         'django.contrib.auth.views.password_reset_done'),
#     url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
#         'django.contrib.auth.views.password_reset_confirm',
#         {'post_reset_redirect' : '/user/password/done/'}),
#     url(r'^user/password/done/$',
#         'django.contrib.auth.views.password_reset_complete'),
#     # url(r'^gerar_pontos/$', 'projetocampeonet.cadastros.views.gerar_pontos', {}, name='gerar_pontos'),
#     url(r'^gerar_pontos/$', 'cadastros.views.gerar_pontos', {}, name='gerar_pontos'),
#
#     # url(r'^logout/$', 'django.contrib.auth.views.logout'),
# )