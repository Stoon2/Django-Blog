from django.contrib import admin
from .models import Post,User, Comment 

from .models import Category, Post,Forbiddenword

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Forbiddenword)
admin.site.register(Comment)
