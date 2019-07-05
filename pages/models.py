from django.db import models
from ckeditor.fields import RichTextField
from Usuarios.models import Interests
from froala_editor.fields import FroalaField

def custom_uptload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.imagen.delete()
    return 'pages/' + filename

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = FroalaField()
    archive = models.FileField(upload_to="media/", null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    interests = models.ManyToManyField(Interests, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
class Intereses(models.Model):
    nombre = models.CharField(max_length = 30)
