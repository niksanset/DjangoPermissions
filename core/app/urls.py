
from django.urls import path
from app.views import create_post, edit_post, delete_post, post_list, post_detail, register,logout_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('create/', create_post, name='create_post'),
    path('edit/<int:post_id>/', edit_post, name='edit_post'),
    path('delete/<int:post_id>/', delete_post, name='delete_post'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]