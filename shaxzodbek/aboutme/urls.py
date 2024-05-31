from django.conf import settings
from django.conf.urls.static import static
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
    path("wish", wish, name='wish'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
