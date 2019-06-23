from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import Egresado, User
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
        

"""
class EgresadoForm(forms.ModelForm):
    name = forms.CharField(label='Nombre:',max_length=15)
    lastname = forms.CharField(label='Apellidos:',max_length=15)
    document = forms.CharField(label='DNI',max_length=12)
    address = forms.CharField(label='Dirección:')
    city = forms.CharField(label='Ciudad:')
    genre = forms.DateField(label='Genero:')
    age = forms.DateField(label = 'Fecha De Nacimiento:')
    email = forms.EmailField(label='Email:',max_length=254)
    class Meta:
        model = Egresado
        fields = ['name','lastname','document','address','city','genre','age']
        labels = {
            'name' : 'Nombre',
            'lastname' : 'Apellidos',
            'document' : 'Documento',
            'address' : 'Dirección',
            'city' : 'Ciudad',
            'genre' : 'Genero',
            'age' : 'Edad'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'lastname': forms.TextInput(attrs={'class':'form-control'}),
            'document': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'genre': forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class':'form-control'}),
        }
"""        


class EgresadoSignUpForm(UserCreationForm):
    YEARS= [x for x in range(1960,2001)]
    
    datebirth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    country = forms.CharField(max_length= "30")


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'genre', 'phone', 'email','username',]
        

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        user.is_Egresado = True
        user.save()
        egresado = Egresado.objects.create( user = user,
                                    country=data['country'],                                  
                                   datebirth=data['datebirth'],
                                   
                                   )
        egresado.save()
    
        return user

class AdmonSignUpForm(UserCreationForm):    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'phone','genre', 'email','username',]

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        user.is_Admon = True
        user.save()     
    
        return user