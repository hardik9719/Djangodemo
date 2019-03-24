from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('/user/create',views.create_user,name='create_user'),
	path('login',views.login, name = 'login'),
	path('',views.index,name= 'index'),
]
