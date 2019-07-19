from django.contrib import admin
from .models import Egresado,  User, EgresadoConsulta, Interests, Profile, Follower
# Register your models here.


class EgresadoAdmin(admin.ModelAdmin):
    list_display = ('country', 'datebirth')


admin.site.register(Egresado, EgresadoAdmin)

class FollowerAdmin(admin.ModelAdmin):
    list_display = ('user', 'account')


admin.site.register(Follower, FollowerAdmin)

class ProfileAdmin(admin.ModelAdmin):
    display = ('interests')


admin.site.register(Profile, ProfileAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name' , 'is_Admon', 'validate')


admin.site.register(User, UserAdmin)

class EgresadoConsultaAdmin(admin.ModelAdmin):
    list_display = ('document','programa')


admin.site.register(EgresadoConsulta, EgresadoConsultaAdmin)

class InterestsAdmin(admin.ModelAdmin):
    display = ('name')


admin.site.register(Interests, InterestsAdmin)