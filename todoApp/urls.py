from django.urls import path
from . import views

app_name = "todoApp"

urlpatterns = [
    path("", views.home, name="home"),
]
