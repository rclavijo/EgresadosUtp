from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import Egresado, User, Interests
from django.forms import ModelForm


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

      