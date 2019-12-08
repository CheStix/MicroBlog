from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Post
from .forms import PostForm


class PostView(View):
    """Сообщения пользователя"""
    def get(self, request):
        posts = Post.objects.order_by('-id')
        form = PostForm()
        return render(request, 'blog/index.html', {'posts': posts, 'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('posts_view_url')
        else:
            return HttpResponse('error')
