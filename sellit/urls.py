"""sellit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static 
from home_page.views import home_page
from add_products.views import add_product
from products.views import products
from sign_up.views import sign_up_form,profile
from login_logout.views import login,logout
from forgot_password.views import forgot_password,reset_password
from django.contrib.auth import views as auth 



urlpatterns = [
    path('admin/', admin.site.urls),
    #home page urls
    path('home/', home_page, name='home'),
    path('', home_page, name='home'),
    #add_products urls
    path('add/', add_product, name='add'),
    #products urls
    path('products/', products, name='products'),
    #sign_up urls
    path('sign_up/',sign_up_form,name='sign_up'),
    path('sign_up/sign',sign_up_form,name='sign'),
    path('profile/',profile,name='profile'),
    #login_logout urls
    path('login/',login,name='login'),
    path('login/login/',login,name='login'),
    path('logout/',logout,name='logout'),
    # API
    path('api/product/',include('add_products.api.urls', 'add')),
    # forgot_password
    path('login/forgot/',forgot_password,name="forgot"),
    path('reset/reset_password/',reset_password,name="reset"),
    path('reset/',reset_password,name="reset"),





]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 
