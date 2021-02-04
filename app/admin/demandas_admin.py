from django.contrib import admin
from django.utils.html import escape
from django.utils.safestring import mark_safe


class DemandasAdmin(admin.ModelAdmin):

    list_display = ["descricao", "status_da_demanda", "email", "cidade", "anunciante"]
    search_fields = ["descricao", "cidade__cidade", "status", "email"]
    readonly_fields = ['descricao', 'status_da_demanda', 'logradouro', 'complemento', 'bairro', 'cep', 'email',
                       'telefone', 'celular', 'cidade', 'anunciante']
    fieldsets = (
        ("Descrição e Status da Demanda", {"fields": (
            ("descricao",),
            ("status_da_demanda",),
            ("anunciante",),
        )}),
        ("Endereço", {"fields": (
            ("logradouro", ),
            ("complemento", ),
            ("bairro", ),
            ("cep", ),
            ("cidade", )
        )}),
        ("Informações de contato", {"fields": (
            ("email", "telefone", "celular")
        )})
    )

    def status_da_demanda(self, obj):
        if obj.status == "Aberta":
            return mark_safe("<img src='/static/images/baseline-highlight_off.svg'>")
        else:
            return mark_safe("<img src='/static/images/baseline-check_circle_outline.svg'>")

    status_da_demanda.allow_tags = True

    def anunciante(self, obj):
        return obj.user.username

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

