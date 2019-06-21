from django.contrib.auth import login
from django.shortcuts import redirect
from ..forms import AdmonSignUpForm
from ..models import User
from django.views.generic import CreateView

class AdmonSignUpView(CreateView):
    model = User
    form_class = AdmonSignUpForm
    template_name = 'Usuarios/signup_Amon.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    