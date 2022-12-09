from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.


class List(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, default=False)
    slug = models.SlugField
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image')
    excerpt = models.TextField(blank=True)


class Item(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name