from django.shortcuts import render

# Create your views here.
def home(request):
    # Example of normal function below:
    ###################################
    # object_user = ObjectModel.all()
    # context = {'all_users': object_user}
    # return render(request, 'blog_app/home.html', context)
    return render(request, 'blog_app/home.html')

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

