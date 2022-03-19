from http.client import responses
from urllib import response
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CategoryForm 
from django.contrib.auth.decorators import login_required

# Create your views here.
#def home(request):
    # Example of normal function below:
    ###################################
    # object_user = ObjectModel.all()
    # context = {'all_users': object_user}
    # return render(request, 'blog_app/home.html', context)
    #return render(request, 'blog_app/home.html')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_app/post.html', {'post': post})


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


@login_required
def add_cat(request):
    # if request.user.is_authenticated and request.user.is_superuser:
        form = CategoryForm()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                # return redirect('post_detail',pk=post.pk)
        context = {'form': form}
        return render(request, 'blog_app/add_category.html', context)
    # else:
    #     return redirect('PostDetailView') 
