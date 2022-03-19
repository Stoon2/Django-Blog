import email
from django.db import models
from django.contrib.auth.models import User
from django.forms import PasswordInput

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class User(models.Model):
   username= models.CharField(max_length=150,null=False,unique=True)
   first_name= models.CharField(max_length=150,null=False)
   last_name= models.CharField(max_length=150,null=True)
   email= models.EmailField(max_length=100,unique=True)
   is_block= models.BooleanField(default=False)
   
   def __str__(self) :
       return self.username+''+self.first_name+''+self.last_name+''+self.email+''+self.is_block
