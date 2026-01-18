from django.contrib import admin
from .models import Pagina

@admin.register(Pagina)
class PaginaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "fecha_publicacion")
    search_fields = ("titulo", "subtitulo", "autor__username")
    prepopulated_fields = {"slug": ("titulo",)}
