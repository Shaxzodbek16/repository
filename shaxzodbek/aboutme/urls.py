from django.urls import path
from .views import mainpage

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('all', all_info, name='all-info'),
]