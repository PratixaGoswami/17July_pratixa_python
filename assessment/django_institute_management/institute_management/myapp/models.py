from django.db import models

# Create your models here.
class signupmodel(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=100)
    city=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class add_student(models.Model):
    name=models.CharField(max_length=50)
    age=models.SmallIntegerField()
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()

class teacher(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.BigIntegerField()
    address=models.TextField()

class books(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)   

class club(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

