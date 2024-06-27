from django.contrib import admin
from .models import Authentication


@admin.register(Authentication)
class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user',)
    list_filter = ('user',)
