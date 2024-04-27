from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profile-form', views.profileForm, name='profile-form'),
]
