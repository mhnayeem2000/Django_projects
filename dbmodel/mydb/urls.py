
from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name="homepage"),
    path('delete/<int:uid>',views.delete,name="delete"),
    path('add_user/',views.adduser_view,name="add_user"),
]
