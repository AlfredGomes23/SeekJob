from django.shortcuts import render, redirect
from .forms import JobForm
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


def create_job(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user.recruiter
            job.save()
            return redirect('jobs')  # Redirect to job detail page or wherever you want
    else:
        form = JobForm()
    return render(request, "JobForm.html", {'job_form': form})
