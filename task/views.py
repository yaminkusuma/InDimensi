from django import forms
from django.http.response import HttpResponse
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
    # -----------
def buatproject(req):
    if req.POST:
        nama = req.POST['nama']
        judul = req.POST['judul']
        type_user = req.POST['type_user']
        jenis_jasa = req.POST['jenis_jasa']
        alamat_jasa = req.POST['alamat_jasa']
        price_jasa = req.POST['price_jasa']
        deadline_jasa = req.POST['deadline_jasa']
        catatan = req.POST['catatan']
        models.buatproject.objects.create(nama = nama, judul = judul, type_user = type_user, jenis_jasa = jenis_jasa, alamat_jasa = alamat_jasa, price_jasa = price_jasa, deadline_jasa = deadline_jasa, catatan = catatan)
    buatproject = models.buatproject.objects.all()    
    return render(req, 'home/buatproject.html', {
        'buatproject' : buatproject
    })

def buatprojecthapus(req, id):
    models.buatproject.objects.filter(id=id).delete()
    return redirect('/buatp')
def buatprojectedit(request, id):
    if request. POST:
        input = request.POST[ "nama"]
        print(input)
        models.buatproject.objects.filter(id = id).update(nama = input)
        return redirect('/')
    data = models.buatproject.objects.filter(id = id).first()
    # return render(request,"buatproject/edit.html",{
    #    "detailData": data,
    # })
    return HttpResponse("cuek")
# ---------------------------------------
def project_lama(req):
    return render(req, 'home/project_lama.html')
def menjadi_worker(req):
    return render(req, 'home/menjadi_worker.html')

# nav jasa
def carijasa(req):
    return render(req, 'home/carijasa.html')
    # -----------
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
