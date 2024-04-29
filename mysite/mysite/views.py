from django.shortcuts import render
from jobs.models import Category
from jobs.models import Job


def home(request):
    categories = Category.objects.all()
    jobs = Job.objects.order_by('-published')[:5]
    return render(request, 'Home.html',  {'user': request.user, "categories": categories, "jobs": jobs})


def contact(request):
    return render(request, 'ContactUS.html')

