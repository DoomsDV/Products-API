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

urlpatterns += [
    path('sub-categories/', sub_categories_api_view,
         name='list-sub-categories-url'),
    path('sub-category/<int:id>/', get_sub_category_api_view,
         name='get-sub-category-url'),
    path('sub-categories/filter/category/<int:id>/',
         filter_sub_category_api_view, name='filter-sub-category-url'),
]

urlpatterns += [
    path('brands/', brands_api_view, name='list-brands-url'),
    path('brand/<int:id>/', get_brand_api_view, name='get-brand-url'),
]
