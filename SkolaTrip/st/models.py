from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True, null=True, default='')
    phone_number = models.CharField(max_length=100, blank=True, null=True, default='')
    class_name = models.CharField(max_length=255, blank=True, null=True, default='')
    student_count = models.PositiveIntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

class ExcursionRegistration(models.Model):
    # Part 1
    school = models.CharField(max_length=255, default='', verbose_name="სახელი გვარი")
    city = models.CharField(max_length=255, default='', verbose_name="მოგზაურობის დაწყების ადგილი")
    destination = models.CharField(max_length=255, default='', verbose_name="სასურველი მოგზაურობის დასრულების ადგილი")
    excursion_type = models.CharField(max_length=100, default='', verbose_name="ექსკურსიის ტიპი")
    accommodation_type = models.CharField(max_length=100, default='', verbose_name="დარჩენის ტიპი")

    # Part 2
    excursion_date = models.DateField(default=timezone.now, verbose_name="სასურველი თარიღი")
    approximate_age = models.CharField(max_length=100, default='', verbose_name="დაახლოებითი ასაკი")
    transportation = models.CharField(max_length=255, default='', verbose_name="ტრანსპორტირების ტიპი")
    probable_length = models.CharField(max_length=100, default='', verbose_name="სავარაუდო ხანგრძლივობა")

    # Part 3
    budget = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, verbose_name="საშუალო ბიუჯეტი")
    food = models.TextField(default='', verbose_name="კვების მოთხოვნები")
    activities = models.TextField(default='', verbose_name="დამატებითი აქტივობები")
    comment = models.TextField(blank=True, null=True, default='', verbose_name="კომენტარი")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.school} excursion to {self.destination} on {self.excursion_date}"
    
class Hotel(models.Model):
    name = models.CharField(max_length=255, default='')
    address = models.CharField(max_length=255, default='')
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=100, blank=True, null=True, default='')
    email = models.EmailField(blank=True, null=True, default='')
    website = models.URLField(blank=True, null=True, default='')
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pool = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    breakfast_included = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True, default='')
    gym = models.BooleanField(default=False)
    spa = models.BooleanField(default=False)
    terrace = models.BooleanField(default=False)
    caffe = models.BooleanField(default=False)
    restaurant = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Driver_info(models.Model):
    name = models.CharField(max_length=255, default='')
    phone_number = models.CharField(max_length=100, blank=True, null=True, default='')
    vehicle_type = models.CharField(max_length=100, blank=True, null=True, default='')
    vehicle_plate = models.CharField(max_length=100, blank=True, null=True, default='')
    vehicle_capacity = models.PositiveIntegerField(default=0)
    vehicle_color = models.CharField(max_length=100, blank=True, null=True, default='')

    def __str__(self):
        return f"{self.name} - {self.vehicle_type} ({self.vehicle_plate})"


class Blog(models.Model):
    title = models.CharField(max_length=255, default='')
    content = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    reading_time = models.TextField(default='', blank=True, null=True)
    small_description = models.TextField(default='', blank=True, null=True)
    photo = models.ImageField(upload_to='blog_photos/', blank=True, null=True)

    def __str__(self):
        return self.title