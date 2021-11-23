
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('', views.index),
    path('regis/', views.register),
    path('home/', views.home),
    path('homes/', views.homes),
    path('kat/', views.kat),
    path('det/', views.det),
]
