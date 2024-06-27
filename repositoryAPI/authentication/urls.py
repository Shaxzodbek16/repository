from django.urls import path
from .views import AuthenticationApiView

urlpatterns = [
    path('', AuthenticationApiView.as_view(), name='authentication'),
]
