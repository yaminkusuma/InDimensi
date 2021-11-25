from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('regis/', views.register),
    path('home/', views.home),
    path('', views.index),

    # path('profil/', views.profil)

    path('regis/', views.register),

    path('login/', views.index),

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
    path('customer/', views.customer),
=======
    
    path('det/', views.det),
    path('kat/', views.kat),


    path('about/', views.about),
    

>>>>>>> c8c80910d3036e1dc282b2345ae396d8659ca2bf
]
