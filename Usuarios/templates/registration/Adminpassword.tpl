{% extends "mail_templated/base.tpl" %}

{% block subject %}
Creación Cuenta {{ user.username }}
{% endblock %}

{% block body %}
Tu Cuenta Ha sido Creada para poder Utilizarla, Ingresa tu correo en el siguiente link 
Para crear una nueva contraseña
{% endblock %}

{% block html %}
<p>Tu Cuenta Ha sido Creada para poder Utilizarla, Ingresa tu correo en el siguiente link 
Para crear una nueva contraseña</p>
<a href = "http://127.0.0.1:8000/cuentas/password_reset"> click aqui </a>
tu nombre de usuario para inicio de sesión es: {{user.username}}
{% endblock %}