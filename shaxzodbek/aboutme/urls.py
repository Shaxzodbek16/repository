from django.urls import path
from .views import *


urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('all', all_info, name='all-info'),
    path("aboutme", aboutme, name='aboutme'),
    path("love", love, name='love'),
    path("friends", friends, name='friends'),
    path("family", family, name='family'),
    path("projects", projects, name='projects'),
]
