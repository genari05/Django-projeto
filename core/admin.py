from django.contrib import admin


from .models import Produto


@admin.register(Produto)
class produtoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'slug', 'criador', 'motivador', 'ativo')
