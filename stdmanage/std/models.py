from django.db import models

class Student(models.Model):
    roll = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name
