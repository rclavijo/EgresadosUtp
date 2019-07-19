{% extends "mail_templated/base.tpl" %}

{% block subject %}
Validación Cuenta {{ user.username }}
{% endblock %}

{% block body %}
Tu Cuenta Ha sido Validada
{% endblock %}

{% block html %}
<p>Tu Cuenta Ha sido Validad, ya puedes hacer uso completo de la plataforma , ingresa aqui:</p>
<a href = "http://egresados.pythonanywhere.com/cuentas/inicio_sesion/"> click aqui </a>
{% endblock %}