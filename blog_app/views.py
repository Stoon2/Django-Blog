from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
#def home(request):
    # Example of normal function below:
    ###################################
    # object_user = ObjectModel.all()
    # context = {'all_users': object_user}
    # return render(request, 'blog_app/home.html', context)
    #return render(request, 'blog_app/home.html')

class HomeView(ListView):
    model = Post
    template_name = 'blog_app/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post.html'

def login(request):
    # Example of normal function below:
    ###################################
    # object_user = ObjectModel.all()
    # context = {'all_users': object_user}
    # return render(request, 'blog_app/home.html', context)
    return render(request, 'blog_app/login.html')

def signup(request):
    # Example of normal function below:
    ###################################
    # object_user = ObjectModel.all()
    # context = {'all_users': object_user}
    # return render(request, 'blog_app/home.html', context)
    return render(request, 'blog_app/signup.html')

