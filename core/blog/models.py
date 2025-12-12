from django.db import models
from accounts.models import User
from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='Posts/' ,null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name