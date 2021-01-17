from django.test import TestCase

# Create your tests here.
from .models import add_product


class ProductTestCase(TestCase):
    def setUp(self):
        add_product.objects.create(Category='Electronics',Type='Laptops',Title='Dell vostro 3480',Price=24999,Description='stylissh',Specification='4gb ram ,1tb hdd',Sellit_assured=True)
        add_product.objects.create(Category='Electronics',Type='Laptops',Title='Dell vostro 3481',Price=25999,Description='stylissh',Specification='4gb ram ,1tb hdd',Sellit_assured=True)
        add_product.objects.create(Category='Electronics',Type='Laptops',Title='Dell vostro 3482',Price=26999,Description='stylissh',Specification='4gb ram ,1tb hdd',Sellit_assured=True)
        add_product.objects.create(Category='Electronics',Type='Laptops',Title='Dell vostro 3483',Price=27999,Description='stylissh',Specification='4gb ram ,1tb hdd',Sellit_assured=True)


    def test_product_test(self):
        obj1 = add_product.objects.get(Title='Dell vostro 3480')
        obj2 = add_product.objects.get(Title='Dell vostro 3481')
        obj3 = add_product.objects.get(Title='Dell vostro 3482')
        obj4 = add_product.objects.get(Title='Dell vostro 3483')
        self.assertEqual(obj1.Title,'Dell vostro 3480')
        self.assertEqual(obj2.Title,'Dell vostro 3481')
        # self.assertEqual(obj2.Price,2599)


