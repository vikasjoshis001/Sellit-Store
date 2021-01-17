from add_products.models import add_product
from rest_framework import generics,mixins
from django.db.models import Q
from .serializers import add_productserializer



class add_productAPI(mixins.CreateModelMixin, generics.ListAPIView):

    lookup_field = 'pk'
    serializer_class = add_productserializer

    def get_queryset(self):
        qs = add_product.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(Q(Category=query)|Q(Type=query)|Q(Title=query)|Q(Price=query)|Q(Description=query)|Q(Specification=query)).distinct()
        return qs


    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)