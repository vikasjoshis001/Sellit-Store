from django.shortcuts import render
from add_products.models import add_product

# Create your views here.


# Electronics products
def products(requests,*args,**kwargs):
    obj=add_product.objects.all()
    context={'object':obj}
    return render(requests,"products/products.html",context)