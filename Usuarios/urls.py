from django.urls import include, path

from .views import AdmonSignUpView,  SignInView, UserEgresadoSignupView, AdmonListView, AdmonUpdateView, EgresadoListView

user_patterns = ([
    path('', include('django.contrib.auth.urls')),
    path('inicio_sesion/', SignInView.as_view(), name='Sigin'),
    path('registro/Egresado/',UserEgresadoSignupView.as_view(), name='Egresado_signup'),
    path('consulta/Egresado/',EgresadoListView.as_view(), name='Egresado_consulta'),
    path('registro/Administrador/',AdmonSignUpView.as_view(), name='Administrador_signup'),
    path('consulta/Administrador/',AdmonListView.as_view(), name='Administrador_consulta'),
    path('editar/Administrador/<int:pk>/',AdmonUpdateView.as_view(), name='Administrador_editar'),
], 'user' ) 