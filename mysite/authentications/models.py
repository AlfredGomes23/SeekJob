from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ('recruiter', 'Recruiter'),
        ('candidate', 'Candidate'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Specify unique related_name for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
