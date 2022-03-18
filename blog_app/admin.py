from sre_parse import CATEGORIES
from django.contrib import admin
from .models import Categorie, Post,Forbiddenword

# Register your models here.
admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Forbiddenword)
