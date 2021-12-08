from django import forms
from django.shortcuts import render, redirect
from . import models

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import CreateUserForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

# Create your views here.

def register(req):

    form = CreateUserForm()
    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()

            user = form.cleaned_data.get('username')
            messages.success(req, 'account was created for ' + user)
            return redirect('login')
    context = {'form': form}

    return render(req, 'register/reg.html', context)

def login_f(req):
    if req.method == "POST":
        _username = req.POST['username']
        _password = req.POST['password']
        user = authenticate(req, username=_username, password=_password)
        if user is not None:
            login(req, user)
            print('halo sayang')
            return redirect('/')

    else:
        print('bodoh')

    context = {}
    print(req.user)
    return render(req, 'login/login.html', context)

def logout_f(req):
    logout(req)
    return redirect('/login')

@login_required(login_url='/login')
def index(req):
    nama = req.user
    data = User.objects.filter(username=nama).first()
    print(data)
    return render(req, 'home/home.html', {
        'user' : nama,
    })


def profil(req):
    return render(req, 'profil/profil.html')

def about (req):
    return render(req, 'profil/about.html')


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

def transaksi(req):
    return render(req, 'home/transaksi.html')
