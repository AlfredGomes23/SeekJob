from datetime import date
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.
class Candidate(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='candidate_photos/')
    phone_number = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    current_company = models.CharField(max_length=100,)
    current_role = models.CharField(max_length=100,)
    skills = models.TextField()
    portfolio_link = models.URLField(blank=True)
    experience_on_field = models.PositiveIntegerField()
    resume = models.FileField(upload_to='candidate_resumes/')

    def __str__(self):
        return self.user.username


class Recruiter(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='recruiter_photos/')
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
    company_phone_number = models.CharField(max_length=20)
    established_year = models.DateField()
    website = models.URLField(blank=True)
    tenure = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username + " " + self.company_name

