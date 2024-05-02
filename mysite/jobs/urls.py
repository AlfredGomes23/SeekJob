"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('jobs/<str:sort>', views.jobs, name='jobs'),
    path('job-details/<int:j_id>', views.job_details, name='job-details'),
    path('create-job', views.create_job, name='create-job'),
    path('update-job/<int:j_id>', views.update_job, name='update-job'),
    path('delete-job/<int:j_id>', views.delete_job, name='delete-job'),
    path('search-job', views.job_search, name='search-job'),
    path('category-jobs/<str:keyword>', views.job_category_search, name='category-jobs'),

]
