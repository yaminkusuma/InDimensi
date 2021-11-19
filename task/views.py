from django.shortcuts import redirect, render

# Create your views here.

# def index(req):
#     return render(req, 'Login/login.html')
def index(req):
    return render(req, 'home/home.html')
    return render(req, 'Login/login.html')

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

def homes(req):
    return render(req, 'homes/homes.html')
