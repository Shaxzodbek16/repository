from django.urls import path
from .views import *


urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('all', all_info, name='all-info'),
    path("aboutme", aboutme, name='aboutme'),
    path("love.html", love, name='love.html'),
    path("friends", friends, name='friends'),
    path("family", family, name='family'),
    path("projects.html", projects, name='projects.html'),
    path("wish", wish, name='wish'),
]
