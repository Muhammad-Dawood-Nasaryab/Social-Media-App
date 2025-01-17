from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# This code makes a form for 'SignUp' model 

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

class LogInForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password",)
