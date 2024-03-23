from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.
def login_user(request):
     if request.method == "POST":
          username = request.POST["username"]
          password = request.POST["password"]
          print(username, password)
          user = authenticate(request, username=username, password=password)
          if user is not None:
               login(request, user)
               return redirect("home")
          else:
               messages.success(request, "There was an error occurred.")
               return redirect("login")
     return render(request, "Authentication.html")

def signup_user(request):
     return render(request, "Authentication.html")