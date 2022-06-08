from django.db import models

class User(models.Model):
    Id=models.AutoField(primary_key=True)
    Username=models.CharField(max_length=100)
    email=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=20)
    conformpassword=models.CharField(max_length=20)
# Create your models here.
class Book(models.Model):
    Bookname=models.CharField(max_length=100)
    Author=models.CharField(max_length=100)
    Noofbooks=models.IntegerField()
    Branch=models.CharField(max_length=100)
