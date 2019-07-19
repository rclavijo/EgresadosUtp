from django import forms
from .models import Page, Interests
from froala_editor.widgets import FroalaEditor
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageCreationForm(forms.ModelForm):
    interests = forms.ModelMultipleChoiceField(queryset=Interests.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'label':'intereses'}))
    class Meta:
        model =Page
        fields = ('title', 'content', 'archive','interests')

        