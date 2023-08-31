from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('products/', products_api_view, name='list-products-url'),
    path('product/<int:id>/', product_api_view, name='get-product-url'),
]
