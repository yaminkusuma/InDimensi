from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.index),
    path('regis/', views.register),
    path('home/', views.home),

    path('regis/', views.register),
    path('login/', views.login),

    # nav kategori
    path('minimalis/', views.minimalis),
    path('luxery/', views.luxery),
    path('industrial/', views.industrial),
    path('klasik/', views.klasik),

    # nav project
    path('buatp/', views.buatproject),
    path('carip/', views.cariproject),
    path('projectlama/', views.project_lama),
    path('menjadiwor/', views.menjadi_worker),

    # nav jasa
    path('carijasa/', views.carijasa),
    path('buatjasa/', views.buatjasa),


    path('homes/', views.homes),
    path('profil/', views.profil),
    path('detail/', views.detail),
<<<<<<< HEAD
=======
<<<<<<< HEAD
=======

    path('customer/', views.customer),


>>>>>>> 93f178584b31699c56b770222aa763f7aad25360

    path('customer/', views.customer),
>>>>>>> b63230cc866ba0632e854d6bc1a33a423256deb3
    
    path('det/', views.det),
    path('kat/', views.kat),

    
]
