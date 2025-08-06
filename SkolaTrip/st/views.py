from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import User
from django.contrib.auth.hashers import make_password

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

def classregister(request):
    if request.method == "POST":
        school_name = request.POST.get("school")
        city = request.POST.get("city")
        class_name = request.POST.get("class")
        pupil_count = request.POST.get("pupil_count")
        other_people_count = request.POST.get("other_people_count")
        excursion_date = request.POST.get("excursion_date")
        location = request.POST.get("location")
        transportation = request.POST.get("transportation")
        proboble_length = request.POST.get("proboble_length")
        budget = request.POST.get("budget")
        food = request.POST.get("food")
        activities = request.POST.get("activities")
        comment = request.POST.get("comment")

        if all([
            school_name, city, class_name, pupil_count, other_people_count,
            excursion_date, location, transportation, proboble_length,
            budget, food, activities, comment
        ]):
            print("school_name:", school_name)
            print("city:", city)
            print("class_name:", class_name)
            print("pupil_count:", pupil_count)
            print("other_people_count:", other_people_count)
            print("excursion_date:", excursion_date)
            print("location:", location)
            print("transportation:", transportation)
            print("proboble_length:", proboble_length)
            print("budget:", budget)
            print("food:", food)
            print("activities:", activities)
            print("comment:", comment)

            return redirect("index")

    else:
        return render(request, "classregister.html")