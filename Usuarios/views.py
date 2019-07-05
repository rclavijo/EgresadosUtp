from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .decorators import egresado_required, administrador_required, superusuario_required
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.views.generic.list import ListView
from .forms import AdmonSignUpForm, UserForm, EgresadoSignUpForm
from .models import User, Egresado , EgresadoConsulta 
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, password_reset, password_reset_done , password_reset_confirm, password_reset_complete
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from mail_templated import send_mail

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
        datos = form.cleaned_data        
        #subject, from_email, to = 'Creación Cuenta', 'proyectolabsw2019@gmail.com', correo
        #text_content = 'Tu Cuenta Ha sido Creada para poder Utilizarla, Ingresa tu correo en el siguiente link Para crear una nueva contraseña'
        #html_content = "<p>{{ protocol }}://{{ domain }}{% url 'user:password_reset'%} tu nombre de usuario para inicio de sesión es: {{user.username}}</p>"
        #msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        #msg.attach_alternative(html_content, "text/html")
        #msg.send()
        user = form.save()                
        login(self.request, user)
        correo = datos ['email']
        username = datos['username']
        send_mail('registration/Adminpassword.tpl', {}, 'proyectolabsw2019@gmail.com',
                     [correo],subject= 'Creación Cuenta')  
        return redirect('pages:pages')    

class SolicitudesListView(UpdateView):
    model = Egresado

class EgresadoListView(ListView):
    model = User   
    def get_queryset(self):
        query = self.request.GET.get("d", None)        
        if query is not None:
            return User.objects.filter(Q(is_Egresado=True) & Q(document = query))
        else:
            return User.objects.filter(is_Egresado=True)              
    template_name = 'egresado_list.html'

class EgresadoConsultaListView(ListView):
    model = User
    query = EgresadoConsulta.objects.values_list('document')  
    queryset = User.objects.filter(Q(is_Egresado=True) & ~Q(document__in=query))
    context_object_name = 'EgresadosNo_list'
    def get_context_data(self, *args, **kwargs):
        context = super(EgresadoConsultaListView, self).get_context_data(*args, **kwargs)
        query = EgresadoConsulta.objects.values_list('document')     
        context['EgresadosEncontrados_list'] = User.objects.filter(Q(is_Egresado=True) & Q(document__in=query))
        return context                      
    template_name = 'egresado_Consultalist.html'
    
@method_decorator(login_required, name='dispatch')
class AdmonListView(ListView):
    model = User    
    queryset = User.objects.filter(is_Admon=True)
    template_name = 'admon_list.html'

@method_decorator([login_required, superusuario_required], name='dispatch')
class AdmonUpdateView(UpdateView):
    model = User
    queryset = User.objects.filter(is_Admon=True)
    fields = ['first_name','last_name','document','gender','phone','city','address']
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

        
   
