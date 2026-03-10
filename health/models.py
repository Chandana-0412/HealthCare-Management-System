from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)   # email unique
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name