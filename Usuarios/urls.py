from django.urls import include, path, re_path
from django.contrib.auth.views import LoginView, logout, password_reset, password_reset_done , password_reset_confirm, password_reset_complete
from .views import AdmonSignUpView,  SignInView, UserEgresadoSignupView, AdmonListView, AdmonUpdateView, EgresadoListView, EgresadoConsultaListView
from django.contrib import auth
from django.urls import reverse, reverse_lazy

user_patterns = ([
    #path('', include('django.contrib.auth.urls')),
    path('inicio_sesion/', SignInView.as_view(), name='Sigin'),
    path('salir/', logout,{'template_name': 'login.html'}, name='Sigout'),
    re_path(r'^password_reset/$', password_reset,{'email_template_name':'registration/password_reset_email.html',
                                                    'template_name':'registration/password_reset_form.html',
                                                    'post_reset_redirect':'user:password_reset_done',
                                            
                                                    },name='password_reset'),

    re_path(r'^password_reset/done/$',password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='password_reset_done'),

    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm,
                                                    {'template_name': 'registration/password_reset_confirm.html',
                                                    'post_reset_redirect': 'user:password_reset_complete'},
                                                    name='password_reset_confirm'),

    re_path(r'^reset/done/$', password_reset_complete, {'template_name': 'registration/password_reset_complete.html'},name='password_reset_complete'),
    path('registro/Egresado/',UserEgresadoSignupView.as_view(), name='Egresado_signup'),
    path('consulta/Egresado/',EgresadoListView.as_view(), name='Egresado_consulta'),
    path('validad/Egresado/',EgresadoConsultaListView.as_view(), name='Egresado_validate'),
    path('registro/Administrador/',AdmonSignUpView.as_view(), name='Administrador_signup'),
    path('consulta/Administrador/',AdmonListView.as_view(), name='Administrador_consulta'),
    path('editar/Administrador/<int:pk>/',AdmonUpdateView.as_view(), name='Administrador_editar'),
], 'user' ) 