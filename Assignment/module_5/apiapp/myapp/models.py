from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    isbn=models.CharField(max_length=50)
    publisher=models.CharField(max_length=50)

