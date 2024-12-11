from django.contrib import admin
from livros.models import Livro

# Register your models here.

class LivroFilter(admin.ModelAdmin):
    list_display = ("id", "user", "titulo", "genero", "nota")
    list_display_links = ("id", "user", "titulo", "genero", "nota")
    list_filter = ("titulo", "genero", "nota")
    search_fields = ("titulo", "genero", "nota")

admin.site.register(Livro, LivroFilter)