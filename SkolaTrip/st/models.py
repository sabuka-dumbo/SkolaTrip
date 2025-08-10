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
    # Part 1: ძირითადი ინფორმაცია
    school_name = models.CharField("სახელი გვარი", max_length=255, default='')  # Name and surname
    city = models.CharField("მოგზაურობის დაწყების ადგილი", max_length=255, default='')  # Start location
    class_name = models.CharField("სასურველი მოგზაურობის დასრულების ადგილი", max_length=100, default='')  # End location
    pupil_count = models.PositiveIntegerField("ექსკურსიის ტიპი", default=0)  # Excursion type (number)
    other_people_count = models.PositiveIntegerField("დარჩენის ტიპი", default=0)  # Stay type (number)

    # Part 2: ექსკურსიის დეტალები
    excursion_date = models.DateField("სასურველი თარიღი", default=timezone.now)
    location = models.CharField("დაახლოებითი ასაკი", max_length=255, default='')  # Approximate age
    transportation = models.CharField("ტრანსპორტირების ტიპი", max_length=255, default='')
    probable_length = models.CharField("ექსკურსიის სავარაუდო ხანგრძლივობა", max_length=100, default='')

    # Part 3: ბიუჯეტი
    budget = models.DecimalField("საშუალო ბიუჯეტი", max_digits=10, decimal_places=2, default=0.00)
    food = models.TextField("კვების მოთხოვნები", default='')
    activities = models.TextField("დამატებითი აქტივობები", default='')
    comment = models.TextField("კომენტარი", blank=True, null=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.school_name} | {self.city} → {self.class_name} | {self.excursion_date}"

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