from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='homepage'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('change_pass/', views.change_password, name='change_password'),
    path('change_pass2/', views.change_password_without_old, name='change_password2'),
    path('profile/', views.profile, name='profile'),
    path('profile_update/', views.updateuser, name='profile_update'),
    path('register/', views.register , name='register'),
    path('user_create_success', views.user_create_success, name='user_create_success'),
]
