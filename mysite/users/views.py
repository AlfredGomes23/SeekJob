from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from authentications.models import UserProfile
from .forms import CandidateForm, RecruiterForm
from .models import Candidate, Recruiter


@login_required
def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
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


def profileForm(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_role = user_profile.role

    if user_role == "Candidate":
        if request.method == "POST":
            candidate_form = CandidateForm(request.POST, request.FILES)
            if candidate_form.is_valid():
                candidate = candidate_form.save(commit=False)
                candidate.user = request.user
                candidate.save()
                return redirect("profile")
        else:
            candidate_form = CandidateForm()

        return render(request, "ProfileForm.html", {"candidate_form": candidate_form})

    elif user_role == "Recruiter":
        if request.method == "POST":
            recruiter_form = RecruiterForm(request.POST, request.FILES)
            if recruiter_form.is_valid():
                recruiter = recruiter_form.save(commit=False)
                recruiter.user = request.user
                recruiter.save()
                return redirect("profile")
        else:
            recruiter_form = RecruiterForm()

        return render(request, "ProfileForm.html", {"recruiter_form": recruiter_form})

    return render(request, "ProfileForm.html")


def candidates(request):
    candidates = Candidate.objects.all()
    return render(request, "Candidates.html", {"candidates": candidates})


def candidate_details(request, u_id):
    user = User.objects.get(pk=u_id)
    candidate = Candidate.objects.get(user=user)
    return render(request, "CandidateDetails.html", {"candidate": candidate})
