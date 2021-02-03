from django.contrib import admin
from ..models import Cidades, Demandas
from .cidades_admin import CidadesAdmin
from .demandas_admin import DemandasAdmin

# Register your models here.
admin.site.register(Cidades, CidadesAdmin)
admin.site.register(Demandas, DemandasAdmin)
