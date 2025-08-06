from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    student_count = models.PositiveIntegerField(blank=True, null=True)