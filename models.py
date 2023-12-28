from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    degree=models.CharField(max_length=20)
    course=models.CharField(max_length=20)

class Placement(models.Model):
    candidate=models.CharField(max_length=20)
    image=models.ImageField(upload_to="")

class Interview(models.Model):
    date = models.DateField()
    description=models.CharField(max_length=500)
