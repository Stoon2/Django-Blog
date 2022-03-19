from django.urls import path
from . import views
from .views import HomeView, PostDetailView

urlpatterns = [
    path('login', views.loginPG, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('signup', views.signup, name='signup'),
]