from django.shortcuts import render


# Create your views here.
def login_user(request):
     return render(request, "Authentication.html")

def signup_user(request):
     return render(request, "Authentication.html")