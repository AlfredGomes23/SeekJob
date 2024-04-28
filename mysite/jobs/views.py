from django.shortcuts import render
from .models import Job
from authentications.models import UserProfile


# Create your views here.
def jobs(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_role = user_profile.role
    jobs = Job.objects.all()
    return render(request, "Jobs.html", {"jobs": jobs, "role": user_role})
