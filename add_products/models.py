from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User,auth


# Create your models here.

class add_product(models.Model):
    Category       = models.CharField(max_length=120)
    Type           = models.CharField(max_length=120)
    Title          = models.CharField(max_length=120)
    Price          = models.DecimalField(decimal_places=2,max_digits=100)
    Description    = models.TextField(blank=False,null=False)
    Specification  = models.TextField(blank=False,null=False)
    Sellit_assured = models.BooleanField(blank=False,null=False)
    Image          = models.ImageField(upload_to="images/",blank=True,null=False)



    def __str__(self):
        return self.Title



