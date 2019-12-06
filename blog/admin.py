from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    """Сообщения"""
    list_display = ('id', 'user', 'text', 'date')
    list_filter = ('user', 'date')


admin.site.register(Post, PostAdmin)
