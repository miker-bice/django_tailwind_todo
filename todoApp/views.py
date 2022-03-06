from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoList


# Create your views here.
def home(request):
    all_todo_items = TodoList.objects.all()
    return render(request, "todoApp/home.html", {'all_items': all_todo_items})


def add_item(request):
    item = request.POST['taskInput']
    new_item = TodoList(item=item)
    new_item.save()
    return HttpResponseRedirect('/todo-app/')


def delete_item(request, item_id):
    item = TodoList.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/todo-app/')
