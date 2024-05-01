from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from authentications.models import UserProfile
from .forms import CandidateForm, RecruiterForm
from .models import Candidate, Recruiter
from django.contrib import messages


@login_required
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        return render(request, "Profile.html", {"role": "Superuser"})
    user_role = user_profile.role

    if user_role == "Candidate":
        candidate = Candidate.objects.get(user=request.user)
        return render(request, "Profile.html", {"role": user_role, "candidate": candidate})
    elif user_role == "Recruiter":
        try:
            recruiter = Recruiter.objects.get(user=request.user)
        except Recruiter.DoesNotExist:
            recruiter = None
        return render(request, "Profile.html", {"role": user_role, "recruiter": recruiter})
    else:
        return render(request, "Profile.html", {"role": user_role})


@login_required
def profileForm(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
        user_role = user_profile.role
    except UserProfile.DoesNotExist:
        messages.error(request, "Something is wrong")
        return render(request, "Profile.html", {"role": "Superuser"})

    if user_role == "Candidate":
        try:
            candidate_profile = Candidate.objects.get(user=request.user)
            if request.method == "POST":
                candidate_form = CandidateForm(request.POST, request.FILES, instance=candidate_profile)
                if candidate_form.is_valid():
                    candidate_form.save()
                    messages.success(request, "Profile Updated.")
                    return redirect("profile")
            else:
                candidate_form = CandidateForm(instance=candidate_profile)
        except Candidate.DoesNotExist:
            if request.method == "POST":
                candidate_form = CandidateForm(request.POST, request.FILES)
                if candidate_form.is_valid():
                    candidate = candidate_form.save(commit=False)
                    candidate.user = request.user
                    candidate.save()
                    messages.success(request, "Profile Created.")
                    return redirect("profile")
            else:
                candidate_form = CandidateForm()

        return render(request, "ProfileForm.html", {"candidate_form": candidate_form})

    elif user_role == "Recruiter":
        try:
            recruiter_profile = Recruiter.objects.get(user=request.user)
            if request.method == "POST":
                recruiter_form = RecruiterForm(request.POST, request.FILES, instance=recruiter_profile)
                if recruiter_form.is_valid():
                    recruiter_form.save()
                    messages.success(request, "Profile Updated.")
                    return redirect("profile")
            else:
                recruiter_form = RecruiterForm(instance=recruiter_profile)
        except Recruiter.DoesNotExist:
            if request.method == "POST":
                recruiter_form = RecruiterForm(request.POST, request.FILES)
                if recruiter_form.is_valid():
                    recruiter = recruiter_form.save(commit=False)
                    recruiter.user = request.user
                    recruiter.save()
                    messages.success(request, "Profile Created.")
                    return redirect("profile")
            else:
                recruiter_form = RecruiterForm()

        return render(request, "ProfileForm.html", {"recruiter_form": recruiter_form})

    return render(request, "ProfileForm.html")



@login_required
def candidates(request):
    candidates = Candidate.objects.all()
    return render(request, "Candidates.html", {"candidates": candidates})


@login_required
def candidate_details(request, c_id):
    try:
        candidate = Candidate.objects.get(pk=c_id)
    except Candidate.DoesNotExist:
        messages.error(request, "Something is wrong.")
        candidate = None
    return render(request, "CandidateDetails.html", {"candidate": candidate})


@login_required
def recruiter_details(request, r_id):
    try:
        recruiter = Recruiter.objects.get(pk=r_id)
    except Recruiter.DoesNotExist:
        messages.error(request, "Something is wrong.")
        recruiter = None
    return render(request, "RecruiterDetails.html", {"recruiter": recruiter})