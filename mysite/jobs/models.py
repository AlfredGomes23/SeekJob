from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models
from users.models import Recruiter


class Category(models.Model):
    category = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category


class Location(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, validators=[MinLengthValidator(3)])
    country = models.CharField(max_length=100, blank=False, null=False, validators=[MinLengthValidator(3)])

    def __str__(self):
        return f"{self.name}, {self.country}"


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
    role = models.CharField(max_length=25, blank=False, null=False)
    details = models.TextField(blank=False, null=False, validators=[MinLengthValidator(30)])
    photo = models.ImageField(upload_to='job_photos/', blank=False)
    contact_number = models.CharField(max_length=20, blank=False, null=False, validators=[MinLengthValidator(6)])
    deadline = models.DateField(blank=False)
    salary = models.DecimalField(max_digits=7, decimal_places=0, blank=False, validators=[MinValueValidator(100)])
    vacancy = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    published = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="Any")
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE, blank=False, null=False)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.title + " - " + str(self.category) + " - " + self.location

