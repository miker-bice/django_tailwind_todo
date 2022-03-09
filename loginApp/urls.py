from django.urls import path
from . import views

app_name = "loginApp"

urlpatterns = [
    path('', views.home, name='home'),
]