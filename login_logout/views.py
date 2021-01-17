from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Username and Password are not matching")
            return redirect('/login')
    else:
        return render(request,"login_logout/login.html")


def logout(request):
    auth.logout(request)
    return redirect('/home')



