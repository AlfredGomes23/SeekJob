from django.db import models
from users.models import Recruiter


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category


class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full-time', 'Full-time'),
        ('Part-time', 'Part-time'),
        ('Contract', 'Contract'),
        ('Freelance', 'Freelance'),
        ('Internship', 'Internship'),
        ('Temporary', 'Temporary'),
    ]
    GENDER_CHOICES = [
        ('Any', 'Any'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    ]
    title = models.CharField(max_length=255, blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES, default="Full-time ")
    role = models.CharField(max_length=255, blank=False, null=False)
    details = models.TextField(blank=False, null=False)
    photo = models.ImageField(upload_to='job_photos/', blank=False)
    contact_number = models.CharField(max_length=20, blank=False, null=False)
    deadline = models.DateField()
    salary = models.DecimalField(max_digits=7, decimal_places=0, blank=False)
    vacancy = models.PositiveIntegerField()
    published = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Any")
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    location = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.title + " - " + str(self.category) + " - " + self.location

