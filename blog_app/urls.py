from django.urls import path
from . import views
from .views import HomeView, PostDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]