from django.urls import path
from . import views
from .views import HomeView, PostDetailView

urlpatterns = [
    path('login', views.loginPG, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('signup', views.signup, name='signup'),
    # path('add_category/', views.add_cat, name="add_cat"),
    # path('del-cat/<cat_id>', views.del_cat, name='del_cat'),

    path('del-post/<post_id>', views.admin_del_post, name='del_post'),
    path('add-comment' , views.comment , name = 'addcomment' ),

    # Admin Views
    path('blog_admin/', views.admin_home, name='admin_home'),
    path('blog_admin/posts', views.admin_posts, name='admin_posts'),
    path('blog_admin/users', views.admin_users, name='admin_users'),
    path('blog_admin/forbidden', views.admin_forbidden, name='admin_forbidden'),
    path('blog_admin/categories', views.admin_categories, name='admin_categories'),

    # Admin Post CRUD
    path('del-post/<post_id>', views.admin_del_post, name='del_post'),
    path('add-post', views.admin_add_post, name='add_post'),
    path('edit-post/<post_id>', views.admin_update_post, name='edit_post'),
    
    # Admin Categories CRUD
    path('add-category/', views.admin_add_category, name='add_category'),
    path('del-cat/<cat_id>', views.del_cat, name='del_cat'),
    # path('add_fWord', views.AddForbiddenWordForm, name='add_fWord')
    

]
