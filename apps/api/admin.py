from django.contrib import admin
from .models import *

@admin.register(Sub_category)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    filter_horizontal = ['sub_categories']
    search_fields = ['id', 'name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['id', 'name'] 
    list_display_links = ['id', 'name']
    search_fields = ['id', 'name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code', 
                    'brand']
    list_display_links = ['id', 'name']
    list_filter = ['category', 'brand', 'sub_category']
    search_fields = ['id', 'name', 'code']
