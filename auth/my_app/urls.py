from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='homepage'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register , name='register'),
    path('user_create_success', views.user_create_success, name='user_create_success'),
]
