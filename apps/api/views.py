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
