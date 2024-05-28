from django.contrib import admin
from .models import Information


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)
    