from http.client import responses
from unicodedata import category
from urllib import response
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import CategoryForm 
from django.contrib.auth.decorators import login_required
from ast import Not
from email import message
from multiprocessing import context
from pdb import post_mortem
from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages

from django.shortcuts import render
from .models import Post , Forbiddenword
from django.views.generic import ListView, DetailView

def admin_home(request):
    return render(request, 'admin/admin_home.html')

def admin_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'admin/posts_panel.html', context)

def admin_users(request):
    return render(request, 'admin/users_panel.html')

def admin_categories(request):
    return render(request, 'admin/categories_panel.html')

def admin_forbidden(request):
    return render(request, 'admin/forbidden_panel.html')
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

# Create your views here.
# @login_required(login_url='login')
# def home(request):

def filterComment(commint):
    wordList = []
     
    forbiddenWords = Forbiddenword.objects.all()
    
    for word in forbiddenWords.iterator():
        wordList.append(word.name)
        
    for i in range(0 , len(wordList)): 
        capital = wordList[i].upper()
        index1 = commint.find(wordList[i])
        index12 = commint.find(capital)  
        if index1 >=0:
            commint = commint.replace(wordList[i] , "****")
        if index12 >=0:
             commint = commint.replace(capital , "****")
    return HttpResponse(commint)
     
    

class HomeView(ListView):
    model = Post
    template_name = 'blog_app/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post.html'

def loginPG(request):
    # Example of normal function below:
    ###################################
    # object_user = ObjectModel.all()
    # context = {'all_users': object_user}
    # return render(request, 'blog_app/home.html', context)
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.info(request,"Username Or Password incorrect")

        return render(request, 'blog_app/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')


def signup(request):
    # Example of normal function below:
    ###################################
    if request.user.is_authenticated :
        return redirect('home')
    else:
        form =CreateUserForm()
        if request.method == 'POST':
            form= CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(request,'Account created for '+user)
                return redirect('login')
        context ={'form':form}
        # object_user = ObjectModel.all()
        # context = {'all_users': object_user}
        # return render(request, 'blog_app/home.html', context)
        return render(request, 'blog_app/signup.html',context)


def add_cat(request):
    if request.user.is_authenticated and request.user.is_superuser :
        form = CategoryForm()
        if request.method == "POST":
            form = CategoryForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {'form': form}
        return render(request, 'blog_app/add_category.html', context)
    else:
         return redirect('home') 


def del_cat(request, cat_id):
    if request.user.is_authenticated and request.user.is_superuser:
        category = category.objects.get(id=cat_id)
        category.delete()
    return redirect('home')