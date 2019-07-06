from django.contrib.auth.models import AbstractUser
from django.db import models
 

class User(AbstractUser):

  GENRE_CHOICES = [
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('Indefinido', 'Indefinido'),
  ] 
  is_Admon = models.BooleanField(default=False)
  is_Egresado = models.BooleanField(default=False)
  document = models.CharField(verbose_name="Documento", unique = True, max_length = 30)
  address = models.TextField(verbose_name="Dirección", null= True, blank= True)
  city = models.TextField(verbose_name="Ciudad", null= True, blank= True)
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
  interests = models.ManyToManyField(Interests, blank=True)
  created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
  updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
  def __str__(self):
    return self.user.first_name

class EgresadoConsulta(models.Model):
  active = models.BooleanField(default=True)   
  document = models.CharField(verbose_name="Documento", unique = True, max_length = 30)
  programa = models.TextField(verbose_name="Programa", null= True, blank= True)

    
  def __str__(self):
    return self.document




      