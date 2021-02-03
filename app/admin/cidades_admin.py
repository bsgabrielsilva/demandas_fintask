from django.contrib import admin


class CidadesAdmin(admin.ModelAdmin):

    list_display = ["slug", "cidade", "estado", "created_at"]
    search_fields = ["cidade", "estado"]
