from django.urls import path
from . import views


urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('profile-form', views.profileForm, name='profile-form'),
    path('candidates', views.candidates, name='candidates'),
    path('candidate/<int:u_id>', views.candidate_details, name='candidate_details'),
]

