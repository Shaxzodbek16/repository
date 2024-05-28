from django.urls import path
from .views import mainpage, all_info

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('all', all_info, name='all-info'),
]