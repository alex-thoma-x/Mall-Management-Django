from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def homelogin(request):
    error = ""
    rle=-1
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        print(u,p)
        user = authenticate(username=u, password=p)
        print(user.role)        
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
            if user.role==1:
                rle=1
            else:
                rle=2
        except:
            error = "yes"
    d = {'error': error,'role':rle}
    return render(request, 'home/login.html', d)