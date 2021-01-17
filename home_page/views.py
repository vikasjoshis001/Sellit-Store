from django.shortcuts import render
# import random,os

# Create your views here.


def home_page(request,*args,**kwargs):
    return render(request,"home_page/home_page.html",{})
