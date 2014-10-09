__author__ = 'danielsiker'

from django import forms
from django.contrib.auth.models import User
from squish.models import Dater


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = Dater
        fields = ('age', 'gender', 'picture', 'city', 'country')
        exclude = ('paid', 'user')


# class LocationForm(forms.ModelForm):
#
#     class Meta:
#         model = Location
#         fields = ('city', 'country')
#         exclude = ('dater',)

