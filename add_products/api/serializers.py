from rest_framework import serializers
from add_products.models import add_product


class add_productserializer(serializers.ModelSerializer):
    class Meta:
        model    =    add_product
        fields   =  [
            'Category',
            'Type',
            'Title',
            'Price',
            'Description',
            'Specification',
            'Sellit_assured'
        ]