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

def forgot_password(request):
    
    if request.method == "POST":
        email      = request.POST['email']

        if User.objects.filter(email=email).exists():
            subject = 'Sellit | Reset Password'
            message = 'India,s No.1 Online store\n\n\nClick on this link to Reset Password: https://sellit-store.herokuapp.com/reset'
            recepient = request.POST['email']
            send_mail(subject,  message, EMAIL_HOST_USER, [recepient], fail_silently = False)
            return render(request, 'login_logout/Email.html')

        else:
            messages.info(request,"**Email does not exist")
            return render(request,"login_logout/login.html")

    else:
        return render(request,"login_logout/login.html")


def reset_password(request):

    datavalid = True

    if request.method == 'POST':
        username   = request.POST['username']
        password1  = request.POST['password1']
        password2  = request.POST['password2']

        if (password1 == password2):

            while datavalid:
                if User.objects.filter(username=username).exists():
                    pass   
                    datavalid = False

                else:
                    messages.info(request,"**username is wrong")  
                    return redirect("/reset")
                    datavalid = False


            if (len(password1) < 8):
                messages.info(request,"**Password should have atleast 8 characters")
                return redirect("/reset")

            else:
                if request.method == "POST":
                    u = User.objects.get(username=username)
                    u.set_password(password1)
                    u.save()
                    return redirect("/login")


        else:
            messages.info(request, "**Password not Matching")
            return redirect('/reset')

    else:
        return render(request,"login_logout/reset.html")




