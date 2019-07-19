from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import Egresado, User, Interests, Profile
from django.forms import ModelForm
from betterforms.multiform import MultiModelForm


"""
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email')
"""

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username','email',
        ]   
class UserModelForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'gender', 'phone']


class EgresadoModelForm(ModelForm):
    YEARS= [x for x in range(1960,2001)]
    datebirth = forms.DateField( label= "fecha de nacimiento", widget=forms.SelectDateWidget(years=YEARS))
    country = forms.CharField(label= "País",max_length= "30")
    class Meta:
        model = Egresado
        fields = ['country', 'datebirth']


class EgrasadoModelForm(MultiModelForm):
    
    form_classes = {
        'user': UserModelForm,
        'egresado': EgresadoModelForm,
    }

    def save(self, commit=True):
        objects = super().save(commit=False)

        if commit:
            user = objects['user']
            user.save()
            egresado = objects['egresado']
            egresado.user = user
            egresado.save()

        return objects


        


class EgresadoSignUpForm(UserCreationForm):
    YEARS= [x for x in range(1960,2001)]
    datebirth = forms.DateField( label= "fecha de nacimiento", widget=forms.SelectDateWidget(years=YEARS))
    country = forms.CharField(label= "País",max_length= "30")
    email = forms.EmailField(required = True,  label = 'email',help_text = "Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'gender', 'phone', 'email','username']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, prueba con otro")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2   

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        user.validate = False
        user.is_Egresado = True
        user.save()
        egresado = Egresado.objects.create( user = user,
                                    country=data['country'],                                  
                                   datebirth=data['datebirth'],
                                   
                                   )
        egresado.save()    
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('document','email', 'last_login', 'validate','groups','date_joined', 'is_superuser','username','password','is_Admon','is_Egresado','user_permissions','is_staff', 'is_active')

class EgresadoUpdateForm(forms.ModelForm):
    email = forms.EmailField(required = True,  label = 'email',help_text = "Requerido, 254 caracteres como máximo y debe ser válido")
    class Meta:
        model = User
        exclude = ( 'last_login', 'validate','groups','date_joined', 'is_superuser','username','password','is_Admon','is_Egresado','user_permissions','is_staff', 'is_active', 'city','gender','address','phone')
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya existe, prueba con otro")
        return email

class AdmonSignUpForm(UserCreationForm):    
    email = forms.EmailField(required = True,  label = 'email',help_text = "Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'phone','gender', 'email','username']
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya existe, prueba con otro")
        return email
    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        user.is_Admon = True
        user.save()     
    
        return user

class ProfileForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(queryset=Interests.objects.all(),widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Profile
        fields = ['avatar','bio','link', 'interests']
        widgets = {
             'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
             'bio' : forms.Textarea(attrs={'class':'form-control mt-3', 'rows': 3, 'placeholder': 'biografia'}),
             'link' : forms.URLInput(attrs={'class':'form-control mt-3',  'placeholder': 'Enlace'}),
         }

class EmailForm(forms.ModelForm):
    email = forms.EmailField(required = True,  label = 'email',help_text = "Requerido, 254 caracteres como máximo y debe ser válido")
    
    class Meta:
        model = User
        fields =['email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email ya existe, prueba con otro")
        return email