from django.urls import path
from . import views
from .views import HomeView, PostDetailView,tagged

urlpatterns = [
    path('login', views.loginPG, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('', views.HomeView, name='home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('like/<int:pk>', views.LikeView, name='like_post'),
    path('dislike/<int:pk>', views.DislikeView, name='dislike_post'),
    path('signup', views.signup, name='signup'),
    path('picked_category/<category_id>', views.display_posts_category, name='display_category'),
    path('subscribe/<int:pk>', views.SubscribeView, name='sub_to_cat'),
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
    path('del_cat/<cat_id>', views.admin_del_category, name='del_cat'),
    path('edit_cat/<cat_id>', views.admin_edit_category, name='edit_cat'),

    # Admin ForbiddenWord CRUD

    path('add_fWord', views.admin_add_forbiddenWord, name='add_fWord'),
    path('del-fword/<forbiddenWord_id>', views.admin_del_forbiddenWord, name='del_fword'),
    path('del-cat/<cat_id>', views.admin_del_category, name='del_cat'),
    
    # Admin Forbidden Word CRUD
    path('add_fWord', views.admin_add_forbiddenWord, name='add_fWord'),
    path('del_fWord/<forbidden_word_id>', views.admin_del_forbiddenWord, name='del_fWord'),
    
    # Admin Users CRUD
    path('del-user/<user_id>', views.admin_del_user, name='del_user'),
    path('edit-user/<user_id>', views.admin_edit_user, name='edit_user'),
    path('promote-user/<user_id>', views.admin_promote_user, name='promote_user'),
    path('demote-user/<user_id>', views.admin_demote_user, name='demote_user'),
    path('deactivate-user/<user_id>', views.admin_deactivate_user, name='deactivate_user'),
    path('activate-user/<user_id>', views.admin_activate_user, name='activate_user'),
    path('tag/<slug:slug>/', tagged, name="tagged"),

]   
