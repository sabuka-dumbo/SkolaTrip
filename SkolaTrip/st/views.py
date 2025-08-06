from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    return render(request, "index.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "შესვლა წარმატებულია!")
            return redirect("index")  # change "home" to your home page URL name
        else:
            messages.error(request, "მომხმარებლის სახელი ან პაროლი არასწორია.")

    return render(request, "login.html")
def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        class_name = request.POST.get("class_name")
        student_count = request.POST.get("student_count")

        # ✅ validation
        if password1 != password2:
            messages.error(request, "პაროლები არ ემთხვევა.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "ეს მომხმარებლის სახელი უკვე გამოყენებულია.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "ეს ელ-ფოსტა უკვე გამოყენებულია.")
            return render(request, "register.html")

        # ✅ create user
        user = User.objects.create(
            username=username,
            email=email,
            full_name=full_name,
            phone_number=phone_number,
            class_name=class_name,
            student_count=student_count if student_count else 0,
            password=make_password(password1),  # hashes password
        )

        login(request, user)
        messages.success(request, "რეგისტრაცია წარმატებით დასრულდა!")
        return redirect("index")  # replace with your actual homepage url name

    return render(request, "register.html")

def dashboard(request):
    return render(request, "dashboard.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    return render(request, "blogs.html")

def classregister(request):
    return render(request, "classregister.html")