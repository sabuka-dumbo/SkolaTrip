from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('services/', views.services, name="services"),
    path('blog/', views.blog, name="blog"),
    path('classregister/', views.classregister, name="classregister"),
    path('hotel/', views.hotel, name="hotel"),
    path('driver/', views.driver, name="driver"),
    path('trip/', views.trip, name="trip")
]