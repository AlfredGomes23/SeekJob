from django.shortcuts import render
from .models import Job
from authentications.models import UserProfile


# Create your views here.
def jobs(request):
    jobs = Job.objects.all()
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return render(request, "Jobs.html", {"jobs": jobs, "role": "Superuser"})
    user_role = user_profile.role
    return render(request, "Jobs.html", {"jobs": jobs, "role": user_role})
