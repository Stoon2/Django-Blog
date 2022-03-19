from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPG, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('signup', views.signup, name='signup'),
]