from django.urls import path, include
from . import views

urlpatterns = [
  path('add_profile/' , views.profiles , name= 'profile'),
]