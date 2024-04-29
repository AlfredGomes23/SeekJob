from django.shortcuts import render, redirect, reverse
from .forms import JobForm
from .models import Job
from authentications.models import UserProfile
from django.contrib import messages


# Create your views here.
def jobs(request):
    jobs = Job.objects.all()
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return render(request, "Jobs.html", {"jobs": jobs, "role": "Superuser"})
    user_role = user_profile.role
    return render(request, "Jobs.html", {"jobs": jobs, "role": user_role})


def job_details(request, j_id):
    try:
        job = Job.objects.get(pk=j_id)
        user_profile = UserProfile.objects.get(user=request.user)
        user_role = user_profile.role
    except Job.DoesNotExist:
        return render(request, "JobDetails.html", {"job": None, "user_role": None, "user": request.user})
    except UserProfile.DoesNotExist:
        user_role = None

    return render(request, "JobDetails.html", {"job": job, "user_role": user_role,  "user": request.user})


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


def update_job(request, j_id):
    try:
        job = Job.objects.get(pk=j_id)
    except Job.DoesNotExist:
        return messages.error(request, "Something is Wrong.")

    if request.method == "POST":
        form = JobForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user.recruiter
            job.save()
            messages.error(request, "Job Updated..")
            return redirect(reverse('job-details', args=[j_id]))
    else:
        form = JobForm(instance=job)

    return render(request, "JobForm.html", {'job_form': form})


def delete_job(request, j_id):
    try:
        Job.objects.get(pk=j_id).delete()
        messages.error(request, "Job Deleted.")
    except Job.DoesNotExist:
        return messages.error(request, "Something is Wrong.")

    return redirect('jobs')