from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('__admin/', admin.site.urls),
    path('', include('aboutme.urls')),
]
