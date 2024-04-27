from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from authentications.models import UserProfile
from .models import Candidate, Recruiter


# Create your views here.
@login_required
def profile(request):
    candidate = None
    recruiter = None
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user_role = user_profile.role
        if user_role == "Candidate":
            candidate = Candidate.objects.get(user=request.user)
            print(candidate.phone_number)
        elif user_role == "Recruiter":
            recruiter = Recruiter.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_role = None
    return render(request, "Profile.html", {"role": user_role, "candidate": candidate, "recruiter": recruiter})
