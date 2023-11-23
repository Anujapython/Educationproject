from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('',views.demo,name='demo'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('form/',views.form,name='form'),
    path('new/',views.new,name='new'),
    path('new2/', views.new2, name='new2'),
    path('logout/',views.logout,name='logout')
]