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
    path('customer/', views.customer),

=======

    path('customer/', views.customer),
    
>>>>>>> 1705b1f2c9aca811c71ae356f0c5db0d2e1f61bd
    path('det/', views.det),
    path('kat/', views.kat),

    
]
