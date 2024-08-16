from django.db import models

# Create your models here.
class Admin(models.Model):
    blog_name = models.CharField(max_length=20)
    blog_created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    super_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    about = models.CharField(max_length=1000)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    suspended = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_active = models.DateTimeField(auto_now=False, auto_now_add=False)


class Post(models.Model):
    owner = models.BigIntegerField()
    brief = models.CharField(max_length=50)
    details = models.CharField(max_length=10000)
    files = models.CharField(max_length=5000)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True, auto_now_add=False)


class Activity(models.Model):
    user = models.BigIntegerField()
    details = models.CharField(max_length=500)
