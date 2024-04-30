from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import UserProfile, Email, Subscriber


# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect("home")
        else:
            messages.error(request, "There was an error occurred.")
            return redirect("login")
    return render(request, "Authentication.html")


def signup_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        role = request.POST["role"]
        if request.POST["password1"] == request.POST["password2"]:
            password = request.POST["password1"]
            print(username, email, password)
            try:
                new_user = User.objects.create_user(username, email, password)
                print(new_user)
                new_user.save()
                print(role)
                new_user_profile = UserProfile.objects.create(user=new_user, role=role)
                new_user_profile.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect("profile-form")
            except:
                messages.error(request, "User name exist.")
        else:
            messages.error(request, "Password didn't matched.")

    return render(request, "Authentication.html")


@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful.")
    return redirect('home')


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        message = request.POST.get('message')
        Email.objects.create(name=name, email=email, sub=sub, message=message)
        return messages.success(request, "Email Sent.")
    return redirect("contact")


def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        Subscriber.objects.get_or_create(email=email)
        return messages.success(request, "Subscribed.")
    return redirect(request.META.get('HTTP_REFERER', '/'))
