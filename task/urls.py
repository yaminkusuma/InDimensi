from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),

    # path('profil/', views.profil)

    path('regis/', views.register),

    path('regis/home/', views.home),
    path('minimalis/', views.minimalis),
    path('luxery/', views.luxery),
    path('industrial/', views.industrial),
    path('klasik/', views.klasik),


    path('homes/', views.homes),
    path('profil/', views.profil),
    path('detail/', views.detail),

]
