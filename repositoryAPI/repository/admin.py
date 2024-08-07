from django.contrib import admin

from django.contrib import admin
from .models import Person, Wish, Shaxzodbek, YouTube, Game


@admin.register(Person)
class PeopleAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'field', 'phone_number', 'connected_at', 'field', 'where_connected')
	search_fields = ('first_name', 'last_name', 'field', 'where_connected')
	list_filter = ('first_name', 'last_name', 'field')


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'is_fulfilled',)
	search_fields = ('title', 'is_fulfilled',)
	list_filter = ('title', 'is_fulfilled', 'created_at')


@admin.register(Shaxzodbek)
class ShaxzodbekAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'views', 'category', 'wish')
	search_fields = ('title', 'people', 'category', 'wish')
	list_filter = ('title', 'views', 'people', 'category', 'wish', 'created_at')


@admin.register(YouTube)
class YouTubeAdmin(admin.ModelAdmin):
	list_display = ('title', 'description', 'link')
	search_fields = ('title', )
	list_filter = ('title', 'created_at')


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'created_at')
	search_fields = ('name', )
	list_filter = ('name', 'created_at')
