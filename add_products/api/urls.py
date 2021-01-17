from django.urls import path
from .views import add_productAPI


app_name = 'add_products'
urlpatterns = [
    path('<int:pk>/',add_productAPI.as_view(),name="api")
   


]
