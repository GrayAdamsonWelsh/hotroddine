from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)

class Booking(models.Model):
    signup = models.ForeignKey(
        Signup, on_delete=models.CASCADE, related_name="booking")
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    date = models.DateTimeField()
    number = models.IntegerField()
    notes = models.TextField()

