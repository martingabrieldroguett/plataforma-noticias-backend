from django.contrib import admin
from .models import Categoria, Autor, Noticia

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'categoria', 'estado', 'fecha_publicacion')
    list_filter = ('estado', 'categoria')
    search_fields = ('titulo', 'contenido')