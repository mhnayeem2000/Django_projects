from django.urls import path, include
from . import views

urlpatterns = [
  path('add_author/' , views.add_authorr , name= 'add_author'),
]