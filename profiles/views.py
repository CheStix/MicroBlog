from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, View


from profiles.forms import ProfileForm
from .models import Profile


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile_detail.html'

    def get_object(self, queryset=None):
        obj = get_object_or_404(Profile, user=self.request.user)
        if obj.user != self.request.user:
            raise Http404
        return obj


class ProfileEditView(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    model = Profile
    template_name = 'profiles/profile_edit.html'
    success_url = reverse_lazy('profile_view_url')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Profile has been updated!!!')
        return super().form_valid(form)


class AddFollow(View):
    """Подпись на пользователя"""
    def post(self, request):
        pk = request.POST.get('pk')
        user = Profile.objects.get(id=pk)
        user.follow.add(User.objects.get(id=request.user.id))
        user.save()
        return HttpResponse(status=200)

