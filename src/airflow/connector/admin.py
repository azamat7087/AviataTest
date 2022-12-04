from django.contrib import admin
from connector.models import (ProvidersData, ExchangeRate)


class ProvidersDataAdmin(admin.ModelAdmin):

    list_display = ('search_id', 'status', 'created_at', 'updated_at')
    list_display_links = ('search_id', )
    search_fields = ('id', 'search_id',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    autocomplete_fields = ()
    list_filter = ('status', )
    fieldsets = ()

admin.site.register(ProvidersData, ProvidersDataAdmin)


class ExchangeRateAdmin(admin.ModelAdmin):

    list_display = ('id', 'created_at', 'updated_at')
    list_display_links = ('id', 'created_at')
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')
    ordering = ('-created_at',)
    autocomplete_fields = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(ExchangeRate, ExchangeRateAdmin)
