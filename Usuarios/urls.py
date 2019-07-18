from django.urls import include, path, re_path
from django.contrib.auth.views import LoginView, password_change, password_change_done, logout, password_reset, password_reset_done , password_reset_confirm, password_reset_complete
from .views import AdmonSignUpView, EgresadoUpdateView2, admondeshabilitar, admonhabilitar, egresadohabilitar,  egresadodeshabilitar, UserEgresadoUpdateView ,  egresadovalidado, EgresadoDeleteView, SignInView, UserEgresadoSignupView, AdmonListView, AdmonUpdateView,  AdmonUpdateView2,  EgresadoListView, EgresadoConsultaListView, ProfileUpdate, EmailUpdate, change_password
from django.contrib import auth
from django.urls import reverse, reverse_lazy

user_patterns = ([
    #path('', include('django.contrib.auth.urls')),
    path('inicio_sesion/', SignInView.as_view(), name='Sigin'),
    path('salir/', logout,{'template_name': 'login.html'}, name='Sigout'),
    re_path(r'^password_change/$', password_change,{'template_name':'registration/password_change_form.html', 
                                                    'post_change_redirect': 'user:password_change_done',                                          
                                                    },name='password_change'),
    re_path(r'^change/done/$', password_change_done, {'template_name': 'registration/password_change_done.html'},name='password_change_done'),

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
    path('profile/',ProfileUpdate.as_view(), name = 'profile'),
    path('cambiar_email/',EmailUpdate.as_view(), name = 'cambiar_email'),
    #path('validar/Egresado/',EgresadoListpview, name='Egresado_validate'),
    re_path(r'^egresadovalidad/(?P<id_usuario>\d+)/$',egresadovalidado, name='Egresadovalidado'),
    re_path(r'^egresadodeshabilitar/(?P<id_usuario>\d+)/$',egresadodeshabilitar, name='Egresadodeshabilitar'),
    re_path(r'^egresadohabilitar/(?P<id_usuario>\d+)/$',egresadohabilitar, name='Egresadohabilitar'),
    re_path(r'^admondeshabilitar/(?P<id_usuario>\d+)/$',admondeshabilitar, name='Admondeshabilitar'),
    re_path(r'^admonhabilitar/(?P<id_usuario>\d+)/$',admonhabilitar, name='Admonhabilitar'),
    path('Eliminar/Egresado/<int:pk>',EgresadoDeleteView.as_view(), name='Egresado_delete'),
    path('registro/Administrador/',AdmonSignUpView.as_view(), name='Administrador_signup'),
    path('consulta/Administrador/',AdmonListView.as_view(), name='Administrador_consulta'),
    path('editar/Administrador/<int:pk>/',AdmonUpdateView.as_view(), name='Administrador_editar'),
    path('editar/Egresado/<int:pk>/',EgresadoUpdateView2.as_view(), name='Administrador_editaregresado'),
    path('editar/<int:pk>/',AdmonUpdateView2.as_view(), name='Administrador_editar2'),
    path('modificar_cuenta/<int:pk>/',UserEgresadoUpdateView.as_view(), name='Egresado_editar'),
], 'user' ) 