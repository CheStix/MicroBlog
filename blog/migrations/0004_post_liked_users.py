# Generated by Django 3.0 on 2019-12-11 20:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_auto_20191210_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='liked_users',
            field=models.ManyToManyField(related_name='user_liked', to=settings.AUTH_USER_MODEL, verbose_name='Кому понравилось'),
        ),
    ]
