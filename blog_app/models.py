from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(blank=True)
    categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ('-date_created', )

    def __str__(self):
        return self.title + ' | ' + str(self.author)

class Forbiddenword(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
