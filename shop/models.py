from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Item(models.Model):
    name = models.TextField(max_length=50, null=False, blank=False, default=None)
    quantity = models.IntegerField(default=1, null=False, blank=False)
    list = models.ForeignKey('List', on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50, null=False, blank=False, default=None)
    description = models.TextField(max_length=50, null=False, blank=False, default=None)
    dueDate = models.DateField(null=True, blank=True, default=datetime.today)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
