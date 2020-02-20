from django.urls import path

from .views import PostView, Like, AllTwit

urlpatterns = [
    path('', AllTwit.as_view(), name='posts_view_url'),
    path('my/', PostView.as_view(), name='user_posts_url'),
    path('like/', Like.as_view(), name='like_url'),
]
