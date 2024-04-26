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
    age = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(36),
            MinValueValidator(16)
        ]
    )
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    dob = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    skills = models.TextField()
    years_of_experience = models.PositiveIntegerField()
    current_company = models.CharField(max_length=100, default="None")
    current_role = models.CharField(max_length=100, default="None")
    resume = models.FileField(upload_to='candidate_resumes/')
    photo = models.ImageField(upload_to='candidate_photos/')

    def __str__(self):
        return self.user.username


class Recruiter(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(40),
            MinValueValidator(25)
        ]
    )
    phone_number = models.CharField(max_length=20)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    tenure = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='recruiter_photos/')
    company_name = models.CharField(max_length=100)
    company_phone_number = models.CharField(max_length=20)
    website = models.URLField(blank=True)
    established_year = models.DateField()

    def __str__(self):
        return self.user.username + " " + self.company_name
