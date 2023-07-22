from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializer import ProductSerializer
from .models import Product
 
@api_view(['GET'])
def getProduct(request):
    return Response()

@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        result = {
            'code': 200,
            'message': 'success',
            'data': serializer.data,
            'error': null
        }
        return Response(result)
    else:
        result = {
            'code': 400,
            'message': 'error',
            'data': [],
            'error': serializer.errors
        }
        return Response(result)