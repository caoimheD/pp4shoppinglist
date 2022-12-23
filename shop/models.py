from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from datetime import datetime


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False, default=None)
    description = models.TextField()
    list_items = models.TextField(default="", blank=False)
    date = models.DateField(null=True, blank=True, default=datetime.today)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title

