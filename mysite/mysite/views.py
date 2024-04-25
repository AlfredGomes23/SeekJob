from django.shortcuts import render


def home(request):
    return render(request, 'Home.html',  {'user': request.user})


def contact(request):
    return render(request, 'ContactUS.html')

