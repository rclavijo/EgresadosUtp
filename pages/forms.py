from django import forms
from .models import Page, Interests
from froala_editor.widgets import FroalaEditor
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PageCreationForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    interests = forms.ModelMultipleChoiceField(queryset=Interests.objects.all(), widget=forms.CheckboxSelectMultiple())
    class Meta:
        model =Page
        fields = ('title', 'content', 'archive','interests')

        