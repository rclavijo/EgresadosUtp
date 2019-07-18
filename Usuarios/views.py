from django.contrib.auth import login, update_session_auth_hash
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView
from .decorators import egresado_required, administrador_required, superusuario_required
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .forms import AdmonSignUpForm, UserForm, EgresadoSignUpForm, EgresadoUpdateForm,  EgrasadoModelForm,   UserUpdateForm, ProfileForm, EmailForm, EgresadoSignUpForm
from .models import User, Egresado , EgresadoConsulta, Profile
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, password_reset, password_reset_done , password_reset_confirm, password_reset_complete
from django import forms
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.core.mail import EmailMultiAlternatives
from mail_templated import send_mail
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

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
        user = form.save()
        login(self.request, user)
        correo = datos ['email']
        username = datos['username']
        send_mail('registration/Adminpassword.tpl', {}, 'proyectolabsw2019@gmail.com',
                     [correo],subject= 'Creación Cuenta')
        return redirect('pages:pages')

@method_decorator([login_required, administrador_required], name='dispatch')
class EgresadoValidadoView(UpdateView):
    model = Egresado
    success_url = reverse_lazy('user:Egresado_validate')
    fields = ['validate']


@login_required
def egresadovalidado(request, id_usuario):
    user = get_object_or_404(User, pk = id_usuario)
    egresado = get_object_or_404(Egresado, user_id = id_usuario)
    if request.method == 'POST' and 'authorize_user' in request.POST:
        user.validate = True
        user.save()
        query = EgresadoConsulta.objects.values_list('document')
        EgresadosNo_list = User.objects.filter(Q(is_Egresado=True) & Q(validate=False))
        EgresadosEncontrados_list = User.objects.filter(Q(is_Egresado=True) & Q(document__in=query))
        template = get_template('egresado_consultalist1.html')
        ctx = {
        'EgresadosNo_list': EgresadosNo_list,
        'EgresadosEncontrados_list': EgresadosEncontrados_list,
        }

        return HttpResponse(template.render(ctx, request))
        # Send a Success Message to the User
    else:
        return render(request, 'egresado_consultalist1.html')

@login_required
def egresadodeshabilitar(request, id_usuario):
    user = get_object_or_404(User, pk = id_usuario)
    egresado = get_object_or_404(Egresado, user_id = id_usuario)
    def get_queryset(self):
        query = self.request.GET.get("d", None)
        if query is not None:
            return User.objects.filter(Q(is_Egresado=True) & Q(document = query))
        else:
            return User.objects.filter(is_Egresado=True)
    template_name = 'egresado_list.html'

    if request.method == 'POST':
        user.is_active = False
        user.save()
        User_list = User.objects.filter(Q(is_Egresado=True))
        template = get_template('egresado_list.html')
        ctx = {
        'user_list': User_list,
        }

        return HttpResponse(template.render(ctx, request))
        # Send a Success Message to the User
    else:
        return render(request, 'egresado_list.html')


@login_required
def egresadohabilitar(request, id_usuario):
    user = get_object_or_404(User, pk = id_usuario)
    egresado = get_object_or_404(Egresado, user_id = id_usuario)
    def get_queryset(self):
        query = self.request.GET.get("d", None)
        if query is not None and query  != " " :
            return User.objects.filter(Q(is_Egresado=True) & Q(document = query))
        else:
            return User.objects.filter(is_Egresado=True)
    template_name = 'egresado_list.html'

    if request.method == 'POST':
        user.is_active = True
        user.save()
        User_list = User.objects.filter(Q(is_Egresado=True))
        template = get_template('egresado_list.html')
        ctx = {
        'user_list': User_list,
        }

        return HttpResponse(template.render(ctx, request))
        # Send a Success Message to the User
    else:
        return render(request, 'egresado_list.html')

@login_required
def admondeshabilitar(request, id_usuario):
    user = get_object_or_404(User, pk = id_usuario)
    def get_queryset(self):
        query = self.request.GET.get("d", None)
        if query is not None:
            return User.objects.filter(Q(is_Admon=True) & Q(document = query))
        else:
            return User.objects.filter(is_Admon=True)
    template_name = 'admon_list.html'

    if request.method == 'POST':
        user.is_active = False
        user.save()
        User_list = User.objects.filter(Q(is_Admon=True))
        template = get_template('admon_list.html')
        ctx = {
        'user_list': User_list,
        }

        return HttpResponse(template.render(ctx, request))
        # Send a Success Message to the User
    else:
        return render(request, 'admon_list.html')

@login_required
def admonhabilitar(request, id_usuario):
    user = get_object_or_404(User, pk = id_usuario)
    def get_queryset(self):
        query = self.request.GET.get("d", None)
        if query is not None:
            return User.objects.filter(Q(is_Admon=True) & Q(document = query))
        else:
            return User.objects.filter(is_Admon=True)
    template_name = 'admon_list.html'

    if request.method == 'POST':
        user.is_active = True
        user.save()
        User_list = User.objects.filter(Q(is_Admon=True))
        template = get_template('admon_list.html')
        ctx = {
        'user_list': User_list,
        }

        return HttpResponse(template.render(ctx, request))
        # Send a Success Message to the User
    else:
        return render(request, 'admon_list.html')

@method_decorator([login_required, administrador_required], name='dispatch')
class EgresadoListView(ListView):
    model = User
    def get_queryset(self):
        query = self.request.GET.get("d", None)
        if query is not None:
            return User.objects.filter(Q(is_Egresado=True) & Q(document = query))
        else:
            return User.objects.filter(is_Egresado=True)
    template_name = 'egresado_list.html'

@method_decorator([login_required, administrador_required], name='dispatch')
class EgresadoDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('user:Egresado_validate')


@method_decorator([login_required, administrador_required], name='dispatch')
class EgresadoConsultaListView(ListView):
    model = User
    query = EgresadoConsulta.objects.values_list('document')
    queryset = User.objects.filter(Q(is_Egresado=True) & Q(validate=False))
    context_object_name = 'EgresadosNo_list'
    def get_context_data(self, *args, **kwargs):
        context = super(EgresadoConsultaListView, self).get_context_data(*args, **kwargs)
        query = EgresadoConsulta.objects.values_list('document')
        context['EgresadosEncontrados_list'] = User.objects.filter(Q(is_Egresado=True) & Q(document__in=query))
        return context
    template_name = 'egresado_consultalist1.html'

@method_decorator([login_required, superusuario_required], name='dispatch')
class AdmonListView(ListView):
    model = User
    def get_queryset(self):
        query = self.request.GET.get("d", None)
        if query is not None:
            return User.objects.filter(Q(is_Admon=True) & Q(document = query))
        else:
            return User.objects.filter(is_Admon=True)
    template_name = 'admon_list.html'

@method_decorator([login_required, superusuario_required], name='dispatch')
class AdmonUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    queryset = User.objects.filter(is_Admon = True)
    template_name = 'admon_update_form.html'
    def get_success_url(self):
        return reverse_lazy('user:Administrador_editar', args = [self.object.id])

@method_decorator([login_required, administrador_required], name='dispatch')
class AdmonUpdateView2(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'admon_update_form.html'
    def get_success_url(self):
        return reverse_lazy('user:Administrador_editar2', args = [self.object.id])

@method_decorator([login_required, administrador_required], name='dispatch')
class EgresadoUpdateView2(UpdateView):
    model = User
    form_class = EgresadoUpdateForm
    template_name = 'admon_update_form.html'
    def get_success_url(self):
        return reverse_lazy('user:Administrador_editaregresado', args = [self.object.id])

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


# class UserEgresadoUpdateView(UpdateView):
#     model = User
#     form_class = EgresadoSignUpForm
#     template_name = 'egresado_update.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'Egresado'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('pages:pages')

class UserEgresadoUpdateView(UpdateView):
    model = Egresado
    form_class = EgrasadoModelForm
    template_name = 'egresado_update.html'
    success_url = reverse_lazy('pages:pages')

    def get_form_kwargs(self):
        kwargs = super(UserEgresadoUpdateView, self).get_form_kwargs()

        kwargs.update(instance={
            'user': self.object.user,
            'egresado': self.object
        })
        return kwargs



@method_decorator(login_required,name = 'dispatch')
class ProfileUpdate(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('user:profile')
    template_name = 'profile_form.html'

    def get_object(self):
        #Recuperar El Objeto  a Editar
        profile, created = Profile.objects.get_or_create(User=self.request.user)
        return profile

@method_decorator(login_required,name = 'dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('user:profile')
    template_name = 'profile_email_form.html'

    def get_object(self):
        #Recuperar El Objeto  a Editar
        return self.request.user
    def get_form (self, form_class=None):
        form  = super(EmailUpdate,self).get_form()
        #modificar en tiempo real
        form.fields['email'].widget = forms.EmailInput (attrs={'class': 'form-control mb-2', 'placeholder': 'Dirección de Correo'} )
        return form

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user:profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

