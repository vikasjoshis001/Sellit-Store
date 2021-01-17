from django.contrib import admin

# Register your models here.
from .models import add_product

admin.site.register(add_product)