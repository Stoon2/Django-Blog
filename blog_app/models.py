import email
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    subscriptions = models.ManyToManyField(User, related_name='category_subs')

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(null=True, blank=True, upload_to="images/")
    categories = models.ManyToManyField(Category)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    dislikes = models.ManyToManyField(User, related_name='post_dislikes')
    comment_number= models.IntegerField(default=0)
    tags = TaggableManager()


    class Meta:
        ordering = ('-date_created', )

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def total_likes(self):
        return self.likes.count()
    
    def total_dislikes(self):
        return self.dislikes.count()


class Forbiddenword(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return self.name
    


class Comment(models.Model):
    username= models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    post_id = models.ForeignKey(Post , related_name="comments", on_delete=models.CASCADE)
    def __str__(self):
        return self.username
          

       
        
