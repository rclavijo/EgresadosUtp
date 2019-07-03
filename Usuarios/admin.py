from django.contrib import admin
from .models import Egresado,  User, EgresadoConsulta
# Register your models here.

class EgresadoAdmin(admin.ModelAdmin):
    readonly_fields = ('country','datebirth')


admin.site.register(Egresado, EgresadoAdmin)

class UserAdmin(admin.ModelAdmin):
    readonly_fields = ('username','first_name','last_name' , 'is_Admon')


admin.site.register(User, UserAdmin)

class EgresadoConsultaAdmin(admin.ModelAdmin):
    list_display = ('document','programa')


admin.site.register(EgresadoConsulta, EgresadoConsultaAdmin)