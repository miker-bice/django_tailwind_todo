from django.urls import path
from . import views

app_name = "todoApp"

urlpatterns = [
    path('', views.home, name='home'),
    path('add_item', views.add_item, name='add-item'),
]
