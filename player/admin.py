from django.contrib import admin

from .models import Player, Time


class ListPlayers(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'media')
    list_display_links = ('nome',)
    search_fields = ('nome',)
    list_filter = ('posicao', 'time')
    list_per_page = 15


admin.site.register(Time)
admin.site.register(Player, ListPlayers)
