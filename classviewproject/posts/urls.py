from django.urls import path, include
from . import views

urlpatterns = [
  path('add_post/' , views.add_post.as_view(), name= 'add_post'),
]