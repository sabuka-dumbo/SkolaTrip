from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    class_name = models.CharField(max_length=255, blank=True, null=True)
    student_count = models.PositiveIntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # avoids clash
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # avoids clash
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

from django.db import models

class ExcursionRegistration(models.Model):
    school_name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    class_name = models.CharField(max_length=100)
    pupil_count = models.PositiveIntegerField()
    other_people_count = models.PositiveIntegerField()
    excursion_date = models.DateField()
    location = models.CharField(max_length=255)
    transportation = models.CharField(max_length=255)
    probable_length = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    food = models.TextField()
    activities = models.TextField()
    comment = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.school_name} - {self.class_name} excursion on {self.excursion_date}"

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Driver_info(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    vehicle_type = models.CharField(max_length=100, blank=True, null=True)
    vehicle_plate = models.CharField(max_length=100, blank=True, null=True)
    vehicle_capacity = models.PositiveIntegerField(default=0)
    vehicle_color = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.vehicle_type} ({self.vehicle_plate})"