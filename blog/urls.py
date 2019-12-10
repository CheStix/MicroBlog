from django.urls import path

from .views import PostView, Like

urlpatterns = [
    path('', PostView.as_view(), name='posts_view_url'),
    path('like/', Like.as_view(), name='like_url'),
]
