from django.db import models
from accounts.models import User, Profile
from django.contrib.auth import get_user_model
from django.urls import reverse

# User = get_user_model()

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='Posts/' ,null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
    def get_snippet(self):
        return self.content[0:5]
    
    

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name