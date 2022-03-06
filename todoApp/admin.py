from django.contrib import admin
from .models import TodoList


# this is the main list that displays the todo items model
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'item')


# Register your models here.
admin.site.register(TodoList, TodoListAdmin)
