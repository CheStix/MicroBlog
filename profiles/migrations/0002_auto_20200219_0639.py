# Generated by Django 3.0 on 2020-02-19 03:39

from django.conf import settings
from django.db import migrations, models
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follow',
            field=models.ManyToManyField(related_name='follow_user', to=settings.AUTH_USER_MODEL, verbose_name='Подписчики'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=profiles.models.get_avatar_upload_path, verbose_name='Аватар'),
        ),
    ]
