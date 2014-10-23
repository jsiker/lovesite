from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

class Dater(models.Model):
    # dater class extends from user
    user = models.OneToOneField(User, related_name='profile')

    #addition attributes to include
    age = models.IntegerField(max_length=3, help_text='age', null=True, blank=True)
    paid = models.BooleanField(default=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    city = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)

    # override unicode to return something meaningful
    def __unicode__(self):
        return self.user.username


# class Location(models.Model):
#     city = models.CharField(max_length=100)
#     country = models.CharField(max_length=100)
#     dater = models.ForeignKey(Dater, related_name='location')

