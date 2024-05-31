from django.contrib import admin
from .models import Information, People, Wish


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')
    search_fields = ('title', 'category')
    list_filter = ('title', 'category')


@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'who_is', 'phone_number', 'email', 'address', 'city', 'job_title')
    search_fields = ('firstname', 'lastname', "phone_number", "who_is", "job_title")
    list_filter = ('firstname', 'lastname', "job_title", "who_is")


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
