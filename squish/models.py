from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Dater(AbstractUser):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=3, help_text='age', null=True, blank=True)
    paid = models.BooleanField(default=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Location(models.Model):
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    dater = models.ForeignKey(Dater, related_name='location')

##### Snir Example
# class ExampleModel(models.Model):
#     image = models.ImageField(upload_to='static/img', default='static/img/no-image.jpg')


class Document(models.Model):
    docfile = models.FileField(upload_to='img/')