from django.urls import path, include
from MyFirstApp import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
]
