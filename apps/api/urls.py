from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('products/', products_api_view, name='list-products-url'),
    path('product/<int:id>/', get_product_api_view, name='get-product-url'),
]

urlpatterns += [
    path('categories/', categories_api_view, name='list-categories-url'),
    path('category/<int:id>/', get_category_api_view, name='get-category-url'),
]
