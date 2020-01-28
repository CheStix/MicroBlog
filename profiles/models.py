from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


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


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance, id=instance.id)
        instance.profile.save()
