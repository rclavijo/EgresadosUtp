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
        

        


class EgresadoSignUpForm(UserCreationForm):
    YEARS= [x for x in range(1960,2001)]
    
    datebirth = forms.DateField(widget=forms.SelectDateWidget(years=YEARS))
    country = forms.CharField(max_length= "30")


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'gender', 'phone', 'email','username',]
        

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

        
class AdmonSignUpForm(UserCreationForm):    

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name','last_name', 'document','address', 'city', 'phone','gender', 'email','username',]

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = super().save(commit=False)
        user.is_Admon = True
        user.save()     
    
        return user

      