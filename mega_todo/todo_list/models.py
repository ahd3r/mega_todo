from django.db import models

from django.contrib.auth.models import User

class TodoListModel(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
