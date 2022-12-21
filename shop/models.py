from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class Item(models.Model):
    item = models.CharField(null=False, blank=False, max_length=50, default=True)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.item


class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False, default=False)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    items = models.ManyToManyField(Item)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']
