from django.db import models

# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    gender = models.CharField(max_length=6,default="Male")

    class Meta:
        db_table="customers"
#python manage.py makemigrations
#python manage.py migrate