from django.contrib import admin


class DemandasAdmin(admin.ModelAdmin):

    list_display = ["descricao", "status", "email", "cidade"]
    search_fields = ["descricao", "cidade__cidade", "status", "email"]
    readonly_fields = ['descricao', 'status', 'logradouro', 'complemento', 'bairro', 'cep', 'email',
                       'telefone', 'celular', 'cidade', 'user']
    fieldsets = (
        ("Descrição e Status da Demanda", {"fields": (
            ("descricao",),
            ("status",),
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
