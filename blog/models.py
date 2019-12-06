from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Модель записи блог"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateTimeField('Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
