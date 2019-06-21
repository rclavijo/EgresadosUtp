from django.db import models
from ckeditor.fields import RichTextField

def custom_uptload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.imagen.delete()
    return 'pages/' + filename

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    imagen = models.ImageField(upload_to=custom_uptload_to, null = True, blank=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
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
