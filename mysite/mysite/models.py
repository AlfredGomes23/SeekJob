from django.db import models


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
