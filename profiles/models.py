from django.contrib.auth.models import User
from django.db import models


class Profile (models.Model):
    """User profile model"""
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    nickname = models.CharField('Прозвище', max_length=100, null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to='profile/', null=True, blank=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user} - {self.nickname}'
