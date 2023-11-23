from django.db import models

class registers(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class logins(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class formss(models.Model):
    name=models.CharField(max_length=50)
    dob=models.DateField()
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phoneno=models.IntegerField()
    email=models.CharField(max_length=50)
    address=models.TextField()
    department=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
