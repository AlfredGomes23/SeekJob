from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Recruiter', 'Recruiter'),
        ('Candidate', 'Candidate'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f'{self.user.username} - {self.role}'
