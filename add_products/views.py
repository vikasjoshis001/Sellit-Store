from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required



# Create your views here.

from .form import add_product_form
from .models import add_product

@login_required(login_url='/login/')
def add_product(request,*args,**kwargs):
    form = add_product_form(request.POST or None)
    if form.is_valid():
        form.save()
        form = add_product_form()
    context={"form":form}
    return render(request,"add_products/add_product_form.html",context)


