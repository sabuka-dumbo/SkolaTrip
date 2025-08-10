from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import User
from django.contrib.auth.hashers import make_password
from .models import *

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    else:
        return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")  # this is actually email
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "შესვლა წარმატებულია!")
            return redirect("index")  # replace with your homepage URL
        else:
            messages.error(request, "მომხმარებლის სახელი ან პაროლი არასწორია.")

    return render(request, "login.html")

def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        class_name = request.POST.get("class_name")
        student_count = request.POST.get("student_count")

        # ✅ check if passwords match
        if password1 != password2:
            messages.error(request, "პაროლები არ ემთხვევა.")
            return render(request, "register.html")

        # ✅ check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "ეს ელ-ფოსტა უკვე გამოყენებულია.")
            return render(request, "register.html")

        # ✅ create user (username = email)
        user = User.objects.create(
            username=email,  # username is set to email
            email=email,
            full_name=full_name,
            phone_number=phone_number,
            class_name=class_name,
            student_count=student_count if student_count else 0,
            password=make_password(password1),  # hashes password
        )

        login(request, user)
        messages.success(request, "რეგისტრაცია წარმატებით დასრულდა!")
        return redirect("index")  # change to your home URL name

    return render(request, "register.html")


def dashboard(request):
    return render(request, "dashboard.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blogs.html")

def hotel(request):
    return render(request, "hotel.html")


def driver(request):
    return render(request, "driver.html")

def trip(request):
    return render(request, "trip.html")

def classregister(request):
    if request.method == "POST":
        # Get data from form
        school1 = request.POST.get("name")  # სახელი გვარი
        city1 = request.POST.get("city")  # მოგზაურობის დაწყების ადგილი
        destination1 = request.POST.get("destination")  # მოგზაურობის დასრულების ადგილი
        excursion_type1 = request.POST.get("excursion_type")  # ექსკურსიის ტიპი
        accommodation_type1 = request.POST.get("accommodation_type")  # დარჩენის ტიპი
        excursion_date1 = request.POST.get("excursion_date")  # სასურველი თარიღი
        approximate_age1 = request.POST.get("approximate_age")  # დაახლოებითი ასაკი
        transportation1 = request.POST.get("transportation")  # ტრანსპორტირების ტიპი
        probable_length1 = request.POST.get("probable_length")
        budget1 = request.POST.get("budget")  # საშუალო ბიუჯეტი
        food1 = request.POST.get("food")  # კვების მოთხოვნები
        activities1 = request.POST.get("activities")  # დამატებითი აქტივობები
        comment1 = request.POST.get("comment")  # კომენტარი

        # Save to DB
        ExcursionRegistration.objects.create(
            school=school1,
            city=city1,
            destination=destination1,
            excursion_type=excursion_type1,
            accommodation_type=accommodation_type1,
            excursion_date=excursion_date1,
            approximate_age=approximate_age1,
            transportation=transportation1,
            probable_length=probable_length1,
            budget=budget1,
            food=food1,
            activities=activities1,
            comment=comment1,
        )

        return redirect("index")  # Replace with your success URL

    return render(request, "classregister.html")
