from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home),
    path('', views.index),
    path('regis/', views.register),
    path('home/', views.home),

    path('regis/', views.register),
    path('login/', views.login_f),
    path('logout/', views.logout_f),

    # nav kategori
    path('points/', views.pointsaya),
    path('proyeks/', views.proyeksaya),
    path('dashboard/', views.dashboard),
    path('akuns/', views.akun_saya),

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
    
    path('det/', views.det),
    path('kat/', views.kat),
    path('trans/', views.transaksi),

    
]
