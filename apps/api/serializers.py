from rest_framework import serializers
from .models import *


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    sub_categories = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'sub_categories']


class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ['id', 'name']


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()

    class Meta:
        model = Product
        fields = ['id', 'name', 'code', 'description', 'brand',
                  'category', 'sub_category', 'price', 'url_image']
