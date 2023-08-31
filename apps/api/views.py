from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *


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
def product_api_view(req, id):
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
