# urls
from django.contrib import admin
from django.urls import path,include
from . import views 



urlpatterns = [
    path('', views.user_login, name="login"),
    path('home/', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('view_blog/', views.view_blog, name="view_blog"),
    path('add_blog/', views.add_blog, name="add_blog"),
    path('view_thoughts/', views.view_thoughts, name="view_thoughts"),
    path('add_thoughts/', views.add_thoughts, name="add_thoughts"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.user_login, name="login"),  # Updated to user_login
    path('register/', views.register, name="register"),
]