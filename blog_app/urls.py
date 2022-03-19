from django.urls import path
from . import views
from .views import HomeView, PostDetailView, add_cat

urlpatterns = [
    path('login', views.loginPG, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('signup', views.signup, name='signup'),
    path('add_category/', views.add_cat, name="add_cat"),
    # Admin Views
    path('blog_admin/', views.admin_home, name='admin_home'),
    path('blog_admin/posts', views.admin_posts, name='admin_posts'),
    path('blog_admin/users', views.admin_users, name='admin_users'),
    path('blog_admin/forbidden', views.admin_forbidden, name='admin_forbidden'),
    path('blog_admin/categories', views.admin_categories, name='admin_categories')
]
