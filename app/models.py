from django.db import models

# Create your models here.
class Asanas(models.Model):
    Symptoms=models.CharField(max_length=50)
    asana1=models.CharField(max_length=50)
    img1=models.ImageField(null=True,blank=True,upload_to="images/")
    asana2=models.CharField(max_length=50)
    img2=models.ImageField(null=True,blank=True,upload_to="images/")
    asana3=models.CharField(max_length=50)
    img3=models.ImageField(null=True,blank=True,upload_to="images/")

class User_det(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.CharField(max_length=50)
    find=models.CharField(max_length=50)

