from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Модель записи блога"""
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    text = models.TextField('Сообщение', max_length=500)
    date = models.DateTimeField('Дата', auto_now_add=True)
    twit = models.ForeignKey('self', verbose_name='Твит', on_delete=models.SET_NULL, blank=True, null=True)
    like = models.IntegerField('Понравилось', default=0)
    liked_users = models.ManyToManyField(User, related_name='user_liked', verbose_name='Кому понравилось')

    def __str__(self):
        return f'{self.id} - {self.user}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ('-id',)
