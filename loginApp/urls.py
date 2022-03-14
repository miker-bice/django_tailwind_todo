from django.urls import path
from . import views

app_name = "loginApp"

urlpatterns = [
    path('', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
]