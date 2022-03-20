from dataclasses import fields
from pyexpat import model
from re import U
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
import django

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2')