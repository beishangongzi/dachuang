from django.db import models


# Create your models here.

class Introduction(models.Model):
    id = models.CharField(max_length=6, unique=True, null=False, primary_key=True)
    text = models.TextField(max_length=1000)

class Image(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img')