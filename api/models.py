from django.db import models

# Create your models here.

class programmer(models.Model):
    fullname = models.CharField(max_length=50)
    nickname = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(default=True)
    phone = models.CharField(max_length=10 ,null=True,default=None)
    is_active = models.BooleanField(default=True)
    
class student(models.Model):
    name = models.CharField(max_length=20)
    apellid = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    Nficha = models.IntegerField(max_length=7)
    formacion = models.BooleanField(default=True)
    fechadeingreso = models.TimeField(auto_now_add=True)
    