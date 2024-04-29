from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Recruiter', 'Recruiter'),
        ('Candidate', 'Candidate'),
        ('Admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, blank=False, null=False)

    def __str__(self):
        return f'{self.user.username} - {self.role}'


class Email(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    sub = models.CharField(max_length=255, blank=False, null=False)
    message = models.TextField(blank=False, null=False)

    def __str__(self):
        return f"{self.name}, {self.email}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True, blank=False, null=False)

    def __str__(self):
        return self.email
