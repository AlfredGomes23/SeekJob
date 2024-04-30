
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Candidate(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    photo = models.ImageField(upload_to='candidate_photos/', blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    current_company = models.CharField(max_length=100, blank=False, null=False)
    current_role = models.CharField(max_length=100, blank=False, null=False)
    skills = models.TextField(blank=False, null=False)
    portfolio_link = models.URLField(blank=False, null=False)
    experience_on_field = models.PositiveIntegerField(blank=False, null=False)
    resume = models.FileField(upload_to='candidate_resumes/', blank=False, null=False)

    def __str__(self):
        return self.user.username


class Recruiter(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    photo = models.ImageField(upload_to='recruiter_photos/', blank=False, null=False)
    dob = models.DateField(blank=False, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    phone_number = models.CharField(max_length=20, blank=False, null=False)
    company_name = models.CharField(max_length=100, blank=False, null=False)
    company_phone_number = models.CharField(max_length=20, blank=False, null=False)
    established_year = models.DateField(blank=False, null=False)
    website = models.URLField(blank=False, null=False)
    tenure = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return self.user.username + " _ " + self.company_name

