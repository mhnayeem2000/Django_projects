from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
        path( '', views.home , name='homepage' ),
        path( 'registration', views.registration_views , name='registration' ),
        path( 'login', views.userLogin , name='login' ),
        path( 'logout', views.userLogout , name='logout' ),
        path( 'profile', views.userProfile , name='profile' ),
]
