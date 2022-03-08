from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# This model holds all the todo items
class TodoList(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    item = models.TextField(max_length=200, blank=False)
    description = models.TextField(max_length=2000, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.item
