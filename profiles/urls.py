from django.urls import path
from .views import ProfileView, ProfileEditView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile_view_url'),
    path('edit_profile/', ProfileEditView.as_view(), name='profile_edit_url'),
]