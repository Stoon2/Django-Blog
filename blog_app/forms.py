
from django import forms
from . models import Category, Forbiddenword, Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from re import U


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ('username','first_name','last_name','email','password1','password2')


# Posts CRUD forms
class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'picture', 'categories')

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('__all__')


class AddForbiddenWordForm(forms.ModelForm):
    class Meta:
        model = Forbiddenword
        fields = ('__all__')

