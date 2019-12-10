from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Post
from .forms import PostForm


class PostView(View):
    """Сообщения пользователя"""
    def get(self, request):
        posts = Post.objects.filter(twit__isnull=True)
        form = PostForm()
        return render(request, 'blog/index.html', {'posts': posts, 'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post_id = request.POST.get('id', None)
            form = form.save(commit=False)
            form.user = request.user
            if post_id:
                form.twit = Post.objects.get(id=post_id)
            form.save()
            return redirect('posts_view_url')
        else:
            return HttpResponse('error')


class Like(View):
    """Ставим дайк"""
    def post(self, request):
        pk = request.POST.get('pk')
        post = Post.objects.get(id=pk)
        post.like += 1
        post.save()
        return HttpResponse(status=201)
