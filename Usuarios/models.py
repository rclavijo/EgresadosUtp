from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinLengthValidator
from django.dispatch import receiver
from django.db.models.signals import post_save

def custom_uptload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename





class User(AbstractUser):

  GENRE_CHOICES = [
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Indefinido', 'Indefinido'),
  ]
  is_Admon = models.BooleanField(default=False)
  is_Egresado = models.BooleanField(default=False)
  document = models.CharField(verbose_name="Documento", unique = True, max_length = 30)
  address = models.CharField(verbose_name="Dirección", max_length=20, validators=[MinLengthValidator(7)], null= True, blank= True)
  city = models.CharField(verbose_name="Ciudad", max_length=20, validators=[MinLengthValidator(4)], null= True, blank= True)
  gender = models.CharField(verbose_name="Genero", null= True, blank= True, max_length = 30, choices=GENRE_CHOICES)
  phone = models.IntegerField(verbose_name="Telefono", null= True, blank= True)
  validate = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

     
  

  


class Interests(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name


class Egresado(models.Model):
  VALIDATE_CHOICES = [
    ('validado', 'Validado'),
    ('Espera', 'Espera'),
    ('Rechazado', 'Rechazado'),
  ]
  user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
  active = models.BooleanField(default=True)
  country = models.TextField(verbose_name="Pais", null= True, blank= True)
  datebirth = models.DateField(verbose_name="Fecha De Nacimiento", null= True, blank= True)
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

  def __str__(self):
    return self.user.first_name

class Profile(models.Model):
    User = models.OneToOneField(User , on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to=custom_uptload_to, null = True, blank=True)
    interests = models.ManyToManyField(Interests, blank=True, related_name='interested_egresados')
    bio = models.TextField(null = True, blank=True)
    link = models.URLField(max_length=200,null = True, blank=True)

    def followers(self):
     return Follower.objects.filter(account=self).count()

    def following(self):
      return Follower.objects.filter(user=self).count() 

  

    

    

class EgresadoConsulta(models.Model):
  active = models.BooleanField(default=True)
  document = models.CharField(verbose_name="Documento", unique = True, max_length = 30)
  programa = models.TextField(verbose_name="Programa", null= True, blank= True)


  def __str__(self):
    return self.document


class Follower (models.Model):
  user = models.ForeignKey(Profile,
        verbose_name='Seguidor',
        on_delete=models.CASCADE,
        related_name='follower_user'
    )
  account = models.ForeignKey(Profile,
        verbose_name='Cuenta a seguir',
        on_delete=models.CASCADE,
        related_name='following_account'
    )

  def save(self, *args, **kwargs):
       if self.user != self.account:
           super(Follower, self).save(*args, **kwargs)

  class Meta:
       verbose_name = 'Seguidor'
       verbose_name_plural = 'Seguidores'

