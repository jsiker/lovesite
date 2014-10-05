__author__ = 'danielsiker'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from squish.models import Dater


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Dater
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")
        # inherits from usercreation form to check passwords, validation, etc

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            Dater.objects.get(username=username)
        except Dater.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()