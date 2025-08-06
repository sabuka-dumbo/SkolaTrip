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

class Excursion(models.Model):
    school_name = models.CharField(max_length=255, blank=True, null=True)
    excursion_place = models.CharField(max_length=255, blank=True, null=True)
    grade = models.CharField(max_length=255, blank=True, null=True)
    pupil_count = models.PositiveIntegerField(default=0)
    other_people_count = models.PositiveIntegerField(default=0)
    excursion_date = models.DateField(blank=True, null=True)
    destination = models.CharField(max_length=255, blank=True, null=True)
    transportation = models.CharField(max_length=255, blank=True, null=True)
    proboble_lenght = models.CharField(max_length=255, blank=True, null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    food = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.school_name} - {self.excursion_place} ({self.excursion_date})"