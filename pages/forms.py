from django import forms
from .models import Page, Interests

class PageCreationForm(forms.ModelForm):
    content = forms.CharField(widget=FroalaEditor)
    interests = forms.ModelMultipleChoiceField(queryset=Interests.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model =Page
        fields = ('title', 'content', 'archive','interests')

        