from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def profile(request):
    print(request.user.username)
    return render(request, "ProfileForm.html", {"user": request.user})
