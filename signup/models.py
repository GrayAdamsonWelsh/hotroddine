from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)