from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..forms import EgresadoSignUpForm
from ..models import User
from ..decorators import egresado_required

class EgresadoSignUpView(CreateView):
    model = User
    form_class = EgresadoSignUpForm
    template_name = '..Usuarios/signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    