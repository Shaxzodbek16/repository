from django.contrib import admin
from .models import Information


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category')
    list_filter = ('title', 'category')

    