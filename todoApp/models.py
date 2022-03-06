from django.db import models


# Create your models here.
# This model holds all the todo items
class TodoList(models.Model):
    item = models.TextField(max_length=200, blank=False)

    def __str__(self):
        return self.item
