from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req, 'Login/login.html')