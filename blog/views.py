from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.models import User

from .models import Post
from .forms import PostForm


class AllTwit(ListView):
    """Выыод всех сообщений"""
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/index.html'


class PostView(View):
    """Сообщения пользователя"""
    def get(self, request):
        if request.user.is_authenticated:
            posts = Post.objects.filter(twit__isnull=True, user=request.user)
        else:
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
            return redirect('user_posts_url')
        else:
            return HttpResponse('error')


class Like(LoginRequiredMixin, View):
    """Ставим лайк"""
    def post(self, request):
        pk = request.POST.get('pk')
        post = Post.objects.get(id=pk)
        if request.user in post.liked_users.all():
            post.liked_users.remove(User.objects.get(id=request.user.id))
            post.like -= 1
        else:
            post.liked_users.add(User.objects.get(id=request.user.id))
            post.like += 1
        post.save()
        return HttpResponse(status=201)
