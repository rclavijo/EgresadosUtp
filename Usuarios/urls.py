from django.urls import include, path

from .views import AdmonSignUpView,  SignInView, UserEgresadoSignupView

user_patterns = ([
    path('', include('django.contrib.auth.urls')),
    path('inicio_sesion/', SignInView.as_view(), name='Sigin'),
    path('registro/Egresado/',UserEgresadoSignupView.as_view(), name='Egresado_signup'),
    path('registro/Administrador/',AdmonSignUpView.as_view(), name='Administrador_signup'),
], 'user' ) 