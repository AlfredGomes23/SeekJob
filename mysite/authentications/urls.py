from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('signup', views.signup_user, name='signup'),
    path('logout', views.logout_user, name='logout'),
    path('send_email', views.send_email, name='send_email'),
    path('subscribe', views.subscribe, name='subscribe'),
]
