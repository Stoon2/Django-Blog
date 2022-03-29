from http.client import responses
from unicodedata import category
from urllib import response
from xml.etree.ElementTree import Comment
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Post,Category
from django.views.generic import ListView, DetailView
from .forms import AddCategoryForm, AddForbiddenWordForm, CategoryForm, CreatePostForm, EditUserForm 
from django.contrib.auth.decorators import login_required
from ast import Not
from django.http import HttpResponseRedirect

from email import message
from multiprocessing import context
from pdb import post_mortem
from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
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
from django.urls import reverse
from django.db.models import F

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


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'blog_admin/users_panel.html', context)


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_del_user(request, user_id):
    user_id = int(user_id)
    try:
        user_to_del = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect('admin_home')
    user_to_del.delete()
    return redirect('admin_users')


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_edit_user(request, user_id):
    user_id = int(user_id)
    user = User.objects.get(id = user_id)
    form = EditUserForm(instance=user)  
    print(user)
    if request.method=='POST':
        form = EditUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('admin_users')
    context = {'user_form' : form}
    return render(request, 'blog_admin/edit_user.html', context)


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_promote_user(request, user_id):
    user_id = int(user_id)
    try:
        user = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect('admin_home')
    user.is_staff = True
    user.is_admin = True
    user.save()
    return redirect('admin_users')

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_demote_user(request, user_id):
    user_id = int(user_id)
    try:
        user = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect('admin_home')
    user.is_staff = False
    user.is_admin = False
    user.save()
    return redirect('admin_users')


@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_deactivate_user(request, user_id):
    user_id = int(user_id)
    try:
        user = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect('admin_home')
    user.is_active = False
    user.save()
    return redirect('admin_users')

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_activate_user(request, user_id):
    user_id = int(user_id)
    try:
        user = User.objects.get(id = user_id)
    except User.DoesNotExist:
        return redirect('admin_home')
    user.is_active = True
    user.save()
    return redirect('admin_users')


def display_posts_category(request, category_id):
    category_id = int(category_id)
    context = {}
    try:
        # category_requested = Category.objects.get(id=category_id)
        posts = Post.objects.filter(categories__id=category_id)
        categories = Category.objects.all()
    except:
        return redirect('home')
    context = {'posts': posts, 'categories': categories, 'picked_category': category_id}
    return render(request, 'blog_app/categories_home.html', context)

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
     
def HomeView(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {'posts': posts, 'categories': categories}
    return render(request, 'blog_app/home.html', context)

# class HomeView(ListView):
#     model = Post, Category
#     template_name = 'blog_app/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog_app/post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data()
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        total_dislikes = post.total_dislikes()
        
        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        return context

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def DislikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    disliked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        disliked = False
    else:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        post.dislikes.add(request.user)
        disliked = True

    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

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
    context = {'forbidden_word' : forbiddenWord_form}
    if forbiddenWord_form.is_valid():
        forbiddenWord_form.save()
        return redirect('admin_forbidden')
    return render(request, 'blog_admin/add_forbidden.html', context)

@user_passes_test(lambda u:u.is_staff, login_url='login')
def admin_del_forbiddenWord(request, forbidden_word_id):
    forbidden_word = Forbiddenword.objects.get(id=forbidden_word_id)
    forbidden_word.delete()
    return redirect('admin_forbidden')

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
    Post.objects.filter(id=request.POST['p_id']).update(comment_number=F('comment_number') + 1)
    return redirect('post-detail' , request.POST['p_id'] )

