from django import forms
from .models import add_product


class add_product_form(forms.ModelForm):
    class Meta():
        model  = add_product
        fields = ['Category','Type','Title','Price','Description','Specification','Sellit_assured','Image']