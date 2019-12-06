from django.shortcuts import render
from django.views.generic import View

from .models import Post
from .forms import PostForm


class PostView(View):
    """Сообщения пользователя"""
    def get(self, request):
        posts = Post.objects.all()
        form = PostForm()
        return render(request, 'blog/index.html', {'posts': posts, 'form': form})
