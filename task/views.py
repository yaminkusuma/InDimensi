from django.shortcuts import render, redirect


# Create your views here.

def index(req):
    return render(req, 'Login/login.html')

def profil(req):
    return render(req, 'profil/profil.html')