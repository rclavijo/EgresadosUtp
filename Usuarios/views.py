from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .decorators import egresado_required, administrador_required, superusuario_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic.list import ListView
from .forms import AdmonSignUpForm, UserForm, EgresadoSignUpForm
from .models import User, Egresado
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

class SignInView(LoginView):
    template_name = 'login.html'

@method_decorator([login_required, superusuario_required], name='dispatch')
class AdmonSignUpView(CreateView):
    model = User
    form_class = AdmonSignUpForm
    template_name = 'signup_Admon.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Administrador'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pages:pages')    

class SolicitudesListView(UpdateView):
    model = Egresado

class EgresadoListView(ListView):
    model = User
    queryset = User.objects.filter(is_Egresado=True)    
    template_name = 'egresado_list.html'

@method_decorator(login_required, name='dispatch')
class AdmonListView(ListView):
    model = User
    queryset = User.objects.filter(is_Admon=True)
    template_name = 'admon_list.html'

@method_decorator([login_required, superusuario_required], name='dispatch')
class AdmonUpdateView(UpdateView):
    model = User
    queryset = User.objects.filter(is_Admon=True)
    fields = ['first_name','last_name','document','genre','phone','city','address']
    template_name = 'admon_update_form.html'
    def get_success_url(self):
        return reverse_lazy('user:Administrador_editar', args = [self.object.id]) + '?ok'

class UserEgresadoSignupView(CreateView):
    model = User
    form_class = EgresadoSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Egresado'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('pages:pages')

        
   
