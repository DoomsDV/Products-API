from django.contrib import admin
from .models import *

@admin.register(Sub_category)
class SubCategoryAdmin(admin.ModelAdmin):

    class Meta:
        model = Sub_category
        fields = ('id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    sub_categories = SubCategoryAdmin() 

    class Meta:
        model = Category
        fields = ('id', 'name', 'sub_categories')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Brand
        fields = ('id', 'name')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    brand = BrandAdmin()

    class Meta:
        model = Product
        fields = ('id', 'name', 'code', 'description', 'brand', 'price'
                  , 'category', 'sub_category', 'url_image')
