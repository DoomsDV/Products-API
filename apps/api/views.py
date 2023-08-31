from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

# Products API


@api_view(['GET', 'POST'])
def products_api_view(req):
    if req.method == 'GET':
        products = Product.objects.all()
        if products.exists():
            products_serializers = ProductSerializer(products, many=True)
            return Response(products_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No products :/'}, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        product_serializer = ProductSerializer(data=req.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_product_api_view(req, id):
    product = Product.objects.filter(id=id).first()
    if product:
        if req.method == 'GET':
            product_serializer = ProductSerializer(product)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        elif req.method == 'PUT':
            product_serializer = ProductSerializer(product, data=req.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method == 'DELETE':
            product.delete()
            return Response({'msg': 'The product was successfully removed'}, status=status.HTTP_200_OK)
    else:
        return Response({'msg': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND)

# Categories API


@api_view(['GET', 'POST'])
def categories_api_view(req):
    if req.method == 'GET':
        categories = Category.objects.all()
        if categories.exists():
            categories_serializers = CategorySerializer(categories, many=True)
            return Response(categories_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No categories'}, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        categories_serializers = CategorySerializer(data=req.data)
        if categories_serializers.is_valid():
            categories_serializers.save()
            return Response(categories_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(categories_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_category_api_view(req, id):
    category = Category.objects.filter(id=id).first()
    if category:
        if req.method == 'GET':
            category_serializer = CategorySerializer(category)
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        elif req.method == 'PUT':
            category_serializer = CategorySerializer(category, data=req.data)
            if category_serializer.is_valid():
                category_serializer.save()
                return Response(category_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method == 'DELETE':
            category.delete()
            return Response({'msg': 'The category was successfully removed'}, status=status.HTTP_200_OK)
    else:
        return Response({'msg': 'The category does not exist'}, status=status.HTTP_404_NOT_FOUND)

# Sub categorias


@api_view(['GET', 'POST'])
def sub_categories_api_view(req):
    if req.method == 'GET':
        sub_categories = Sub_category.objects.all()
        if sub_categories.exists():
            sub_categories_serializers = SubCategorySerializer(
                sub_categories, many=True)
            return Response(sub_categories_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'No sub categories'}, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        sub_category = SubCategorySerializer(data=req.data)
        if sub_category.is_valid():
            sub_category.save()
            return Response(sub_category.data, status=status.HTTP_201_CREATED)
        else:
            return Response(sub_category.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_sub_category_api_view(req, id):
    sub_category = Sub_category.objects.filter(id=id).first()
    if sub_category:
        if req.method == 'GET':
            sub_category_serializer = SubCategorySerializer(sub_category)
            return Response(sub_category_serializer.data, status=status.HTTP_200_OK)
        elif req.method == 'PUT':
            sub_category_serializer = SubCategorySerializer(
                sub_category, data=req.data)
            if sub_category_serializer.is_valid():
                sub_category_serializer.save()
                return Response(sub_category_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(sub_category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method == 'DELETE':
            sub_category.delete()
            return Response({'msg': 'The sub category was successfully removed'}, status=status.HTTP_200_OK)
    else:
        return Response({'msg': 'The sub category does not exist'}, status=status.HTTP_404_NOT_FOUND)

# Marcas


@api_view(['GET', 'POST'])
def brands_api_view(req):
    if req.method == 'GET':
        brands = Brand.objects.all()
        if brands.exists():
            brands_serializers = BrandSerializer(brands, many=True)
            return Response(brands_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': {'No brands'}}, status=status.HTTP_200_OK)
    elif req.method == 'POST':
        brands_serializers = BrandSerializer(data=req.data)
        if brands_serializers.is_valid():
            brands_serializers.save()
            return Response(brands_serializers.data, status=status.HTTP_200_OK)
        else:
            return Response(brands_serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_brand_api_view(req, id):
    brand = Brand.objects.filter(id=id).first()
    if brand:
        if req.method == 'GET':
            brand_serializer = BrandSerializer(brand)
            return Response(brand_serializer.data, status=status.HTTP_200_OK)
        elif req.method == 'PUT':
            brand_serializer = BrandSerializer(brand, data=req.data)
            if brand_serializer.is_valid():
                brand_serializer.save()
                return Response(brand_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(brand_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif req.method == 'DELETE':
            brand.delete()
            return Response({'msg': 'The brand was successfully removed'}, status=status.HTTP_200_OK)
    else:
        return Response({'msg': 'The brand does not exist'}, status=status.HTTP_404_NOT_FOUND)
