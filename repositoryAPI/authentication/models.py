from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Authentication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authentication')

    def __str__(self):
        return str(self.user)

    class Meta:
        db_table = 'authentication'
        verbose_name = 'Authentication'
        verbose_name_plural = 'Authentications'

