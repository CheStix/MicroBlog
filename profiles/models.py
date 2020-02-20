import os

from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


def get_avatar_upload_path(instance, file):
    """
    :param instance: user profile
    :param file: name user loaded file
    :return: path to save loaded file
    """
    time = timezone.now().strftime('%Y-%m-%d')
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + time + '.' + end_extention
    print(file_name)
    return os.path.join('profile', 'user_{0}', '{1}').format(instance.user.id, file_name)


class Profile (models.Model):
    """User profile model"""
    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    nickname = models.CharField('Прозвище', max_length=100, null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to=get_avatar_upload_path, null=True, blank=True)
    follow = models.ManyToManyField(User, verbose_name='Подписчики', related_name='follow_user')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f'{self.user} - {self.nickname}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            print('Avatar detected')
            img = Image.open(self.avatar.path)
            if img.height > 150 or img.width > 150:
                output_size = (150, 150)
                img.thumbnail(output_size)
                img.save(self.avatar.path)


    @property
    def get_avatar_url(self):
        if self.avatar:
            return f'/media/{self.avatar}'
        else:
            return '/static/img/user_profile_default.png'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Создание профиля пользователя при регистрации"""
    if created:
        Profile.objects.create(user=instance, id=instance.id)
        # instance.profile.save()
