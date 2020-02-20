from django.urls import path
from .views import *


urlpatterns = [
    path('', ProfileView.as_view(), name='profile_view_url'),
    path('edit_profile/', ProfileEditView.as_view(), name='profile_edit_url'),
    path('follow/', AddFollow.as_view(), name='add_follow_url'),
]