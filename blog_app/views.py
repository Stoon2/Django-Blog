from http.client import responses
from unicodedata import category
from urllib import response
from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Post,Category
from django.views.generic import ListView, DetailView
from .forms import AddCategoryForm, AddForbiddenWordForm, CategoryForm, CreatePostForm 
from django.contrib.auth.decorators import login_required
from ast import Not
from django.http import HttpResponseRedirect

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

from django.utils import timezone
from . import models as m

from django.contrib.auth.decorators import user_passes_test


from django.shortcuts import render
from .models import Post , Forbiddenword
from django.views.generic import ListView, DetailView

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_home(request):
    return render(request, 'blog_admin/blog_admin_home.html')

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog_admin/posts_panel.html', context)


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_users(request):
    return render(request, 'blog_admin/users_panel.html')

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_categories(request):
     categories = Category.objects.all()
     context = {'categories': categories}
     return render(request, 'blog_admin/categories_panel.html',context)

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_forbidden(request):
     words = Forbiddenword.objects.all()
     context = {'words': words}
     return render(request, 'blog_admin/forbidden_panel.html',context)

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_del_post(request, post_id):
    post_id = int(post_id)
    try:
        post_to_del = Post.objects.get(id = post_id)
    except Post.DoesNotExist:
        return redirect('admin_home')
    post_to_del.delete()
    return redirect('admin_posts')

    # def del_post(request, post_id):
    # if request.user.is_authenticated and request.user.is_superuser:
    #     post = category.objects.get(id=post_id)
    #     post.delete()
    # return redirect('blog_admin/posts')
@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_add_post(request):
    post_form = CreatePostForm(request.POST)
    context = {'post_form' : post_form}
    if post_form.is_valid():
        post_form.save()
        return redirect('admin_posts')

    return render(request, 'blog_admin/add_post.html', context)

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_update_post(request, post_id):
        post_id = int(post_id)
        post = Post.objects.get(id = post_id)
        form = CreatePostForm(instance=post)  
        if request.method=='POST':
            form = CreatePostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('admin_posts')
        context = {'post_form' : form}
        return render(request, 'blog_admin/edit_post.html', context)
        # return redirect('admin_posts')


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_add_category(request):
    category_form = AddCategoryForm(request.POST)
    context = {'category_form' : category_form}
    if  category_form.is_valid():
        category_form.save()
        return redirect('admin_categories')

    return render(request, 'blog_admin/add_category.html', context)
        

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
           
    
    return (commint)
     
    

class HomeView(ListView):
    model = Post
    template_name = 'blog_app/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post.html'

def loginPG(request):
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
    if request.user.is_authenticated:
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
        return render(request, 'blog_app/signup.html',context)





def del_cat(request, cat_id):
    if request.user.is_authenticated and request.user.is_superuser:
        category = category.objects.get(id=cat_id)
        category.delete()
        # return redirect('blog-index')
    return redirect('blog_admin/categories')


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_add_forbiddenWord(request):
    forbiddenWord_form = AddForbiddenWordForm(request.POST)
    context = {'forbiddenWord_form' : forbiddenWord_form}
    if forbiddenWord_form.is_valid():
        forbiddenWord_form.save()
    return render(request, 'blog_admin/add_post.html', context)



    # def add_cat(request):
#     if request.user.is_authenticated and request.user.is_superuser :
#         form = CategoryForm()
#         if request.method == "POST":
#             form = CategoryForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return redirect('home')
#         context = {'form': form}
#         return render(request, 'blog_app/add_category.html', context)
#     else:
#          return redirect('home') 

# def del_post(request, post_id):
#     if request.user.is_authenticated and request.user.is_superuser:
#         post = category.objects.get(id=post_id)
#         post.delete()
#     return redirect('blog_admin/posts')
def comment(request):
    comm_body=request.POST['body']
    comm_body = filterComment(comm_body)
   
  
    comment = m.Comment(username=request.user.username , body=  comm_body, post_id_id = request.POST['p_id'])
    comment.save()
    return redirect('post-detail' , request.POST['p_id'] )

