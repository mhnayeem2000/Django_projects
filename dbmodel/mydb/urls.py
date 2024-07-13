
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="homepage"),
    path('delete/<int:uid>',views.delete,name="delete"),
]
