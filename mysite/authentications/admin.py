from django.contrib import admin
from .models import UserProfile, Email, Subscriber

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Email)
admin.site.register(Subscriber)
