from django.contrib import admin
from livraria.models import Autor,Livro,Categoria
# Register your models here.


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor')

admin.site.register(Autor)
admin.site.register(Livro,LivroAdmin)
admin.site.register(Categoria)