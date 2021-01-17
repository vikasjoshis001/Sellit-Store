from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import time
#Email
from sellit.settings import EMAIL_HOST_USER
from django.core.mail import send_mail 
from django.core.mail import EmailMultiAlternatives 
from django.template.loader import get_template 
from django.template import Context 

# Create your views here.


def sign_up_form(request):


    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name  = request.POST['first_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password1  = request.POST['password1']
        password2  = request.POST['password2']
 
        if (password1 == password2):
            if User.objects.filter(username=username).exists():
                messages.info(request, "**username already exists")
                return redirect('/sign_up')

            elif User.objects.filter(email=email).exists():
                messages.info(request, "**Email already exists")
                return redirect('/sign_up')

            else:
                if request.method == 'POST':
                    user=User.objects.create_user(username=username,password=password2,email=email,first_name=first_name,last_name=last_name)
                    user.save();
                    subject = 'Welcome to Sellit'
                    message = 'India,s No.1 Online store\n\n\nClick on this link to login: http://127.0.0.1:8000/login'
                    recepient = request.POST['email']
                    send_mail(subject,  message, EMAIL_HOST_USER, [recepient], fail_silently = False)
                    return render(request, 'sign_up/Email.html')
        
        else:
            messages.info(request, "**Password not Matching")
            return redirect('/sign_up')

    else:
        return render(request,"sign_up/sign_up.html")


def profile(request):
    return render(request,"sign_up/profile.html",{})
