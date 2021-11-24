from django.shortcuts import render, redirect
from . import models


# Create your views here.

def index(req):
    return render(req, 'Login/login.html')

def profil(req):
    return render(req, 'profil/profil.html')

def about (req):
    return render(req, 'profil/about.html')

# def login(req):
#     if req.POST:
#         input_email = req.POST['email']
#         input_password = req.POST['password']

#         user = models.login.objects.filter(email=input_email, password=input_password).first()
#         print(user)
#         if user is not None:
#             return redirect('/')
#     data = models.login.objects.all()
#     return render(req, 'Login/login.html', {
#         'data': data,
#     })
def login(req):
    if req.POST:
        input_email = req.POST['email']
        input_password = req.POST['password']

        user = models.login.objects.filter(email=input_email, password=input_password).first()
        print(user)
        if user is not None:
            return redirect('/')
    data = models.login.objects.all()
    return render(req, 'Login/login.html', {
        'data': data,
    })

def register(req):
    return render(req, 'register/reg.html')

def home(req):
    return render(req, 'home/home.html')

def minimalis(req):
    return render(req, 'home/minimalis.html')

def luxery(req):
    return render(req, 'home/luxery.html')

def industrial(req):
    return render(req, 'home/industrial.html')

def klasik(req):
    return render(req, 'home/klasik.html')

def homes(req):
    return render(req, 'homes/homes.html')

def kat(req):
    return render(req, 'katalog/kat.html')

def det(req):
    return render(req, 'katalog/det.html')
def profil(req):
    return render(req, 'profil/profil.html')



def detail(req):
    return render(req, 'detail/detail.html')
