from django.urls import path
from . import views

urlpatterns = [
    path('',          views.index,    name='index'),
    path('newuser',   views.newuser,  name='newuser'),
    path('register/', views.register, name='register'),
    path('home', views.home, name='home'),
    path('do_login/', views.do_login, name='do_login'),
    
    #path('home', views.home, name='home'),
]
