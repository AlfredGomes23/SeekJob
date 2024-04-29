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
