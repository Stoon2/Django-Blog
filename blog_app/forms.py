from django import forms
from .models import Category
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
from dataclasses import fields
from pyexpat import model
from re import U
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models  import User
import django
import django


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)






class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2')
