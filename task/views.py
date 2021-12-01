from django.shortcuts import render, redirect
from . import models


# Create your views here.

def index(req):
    return render(req, 'home/home.html')

def login(req):
    return render(req, 'login/login.html')

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

def register(req):
    return render(req, 'register/reg.html')

def home(req):
    return render(req, 'home/home.html')

# nav kategori
def pointsaya(req):
    return render(req, 'home/pointsaya.html')
def proyeksaya(req):
    return render(req, 'home/proyeksaya.html')
def dashboard(req):
    return render(req, 'home/dashboard.html')
def akun_saya(req):
    return render(req, 'home/akun_saya.html')

# nav project
def cariproject(req):
    return render(req, 'home/cariproject.html')
def buatproject(req):
    return render(req, 'home/buatproject.html')
def project_lama(req):
    return render(req, 'home/project_lama.html')
def menjadi_worker(req):
    return render(req, 'home/menjadi_worker.html')

# nav jasa
def carijasa(req):
    return render(req, 'home/carijasa.html')
def buatjasa(req):
    return render(req, 'home/buatjasa.html')

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
