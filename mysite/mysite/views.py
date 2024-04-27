from django.shortcuts import render
from jobs.models import Category


def home(request):
    categories = Category.objects.all()
    return render(request, 'Home.html',  {'user': request.user, "categories": categories})


def contact(request):
    return render(request, 'ContactUS.html')

