from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *

# Register your models here.
# class LojaAdmin(admin.ModelAdmin):
#     pass

class FormasDePagamentoAdmin(admin.ModelAdmin):
    pass

# class AceitaAdmin(admin.ModelAdmin):
#     pass

# class ProfissionalAdmin(admin.ModelAdmin):
#     pass

class TipoServicoAdmin(admin.ModelAdmin):
    pass

class ServicoAdmin(admin.ModelAdmin):
    pass

class SubservicoAdmin(admin.ModelAdmin):
    pass

class ClienteAdmin(admin.ModelAdmin):
    pass

# class OfereceAdmin(admin.ModelAdmin):
#     pass

class AgendaAdmin(admin.ModelAdmin):
    
    pass

class FotoServicoAdmin(admin.ModelAdmin):

    pass
admin.site.site_header = 'Praça XI - Administração'
admin.site.unregister(Group)
admin.site.unregister(User)

# admin.site.register(Loja, LojaAdmin)
admin.site.register(FormasDePagamento, FormasDePagamentoAdmin)
# admin.site.register(Aceita, AceitaAdmin)
# admin.site.register(Profissional, ProfissionalAdmin)
admin.site.register(TipoServico, TipoServicoAdmin)
admin.site.register(Servico, ServicoAdmin)
#admin.site.register(Subservico, SubservicoAdmin)
admin.site.register(Cliente, ClienteAdmin)
# admin.site.register(Oferece, OfereceAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(FotosServico, FotoServicoAdmin)
