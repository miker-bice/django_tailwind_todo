from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import TodoList
from .forms import TodoForm


# this view handles rendering the home page
def home(request):
    if request.user.is_authenticated:
        all_todo_items = TodoList.objects.filter(user_id=request.user.id)
        return render(request, 'todoApp/home.html', {'all_items': all_todo_items})
    else:
        return redirect('loginApp:login')


# this view handles adding items to the database
def add_item(request):
    item = request.POST['taskInput']
    # the code below only works if the template contains a hidden input with the current id of the logged in user
    # target_id = request.POST['targetId']
    user = User.objects.only('id').get(id=request.user.id)
    new_item = TodoList(user_id=user, item=item)
    new_item.save()
    return HttpResponseRedirect('/todo-app/')


# this view handles item deletion
def delete_item(request, item_id):
    item = TodoList.objects.get(pk=item_id)
    item.delete()
    return HttpResponseRedirect('/todo-app/')


# this view handles the view of specific tasks as well as the update
def task_view(request, item_id):
    if request.user.is_authenticated:
        item = get_object_or_404(TodoList, pk=item_id)
        form = TodoForm(request.POST or None, instance=item)

        if form.is_valid():
            form.save()
            return redirect('todoApp:home')

        # if request.method == 'POST':
        #     form = TodoForm(request.POST)
        #
        #     if form.is_valid():
        #         todo_instance.save()
        #         messages.success(request, "Todo successfully updated")
        #     else:
        #         messages.error(request, "There is an error updating the todo task")
        #
        #     return HttpResponseRedirect('/todo-app/')

        return render(request, 'todoApp/task.html', {'form': form})

    else:
        return redirect('loginApp:login')


# this handles user logout
def user_logout(request):
    logout(request)
    return redirect('loginApp:login')


# this is for the custom 404 error message
def entry_not_found(request, exception):
    return render(request, '404.html', status=404)
