from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add/',views.add,name='add'),
    path('reset/',views.reset,name='reset'),
]