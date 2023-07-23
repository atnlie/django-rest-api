from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import ProductSerializer
from .models import Product

@csrf_exempt
@api_view(['GET'])
def getProduct(request):
    return Response()

@csrf_exempt
@api_view(['GET'])
def getAllProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    result = {
        'code': status.HTTP_200_OK,
        'message': 'success',
        'data': serializer.data,
        'error': ''
    }
    return Response(result)

@csrf_exempt
@api_view(['POST'])
def addProduct(request):
    serializer = ProductSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        result = {
            'code': status.HTPP_201_CREATED,
            'message': 'success',
            'data': serializer.data,
            'error': False
        }
        return Response(result)
    else:
        result = {
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors,
            'data': [],
            'error': True
        }
        return Response(result)

@csrf_exempt
@api_view(['GET', 'POST'])
def product(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        result = {
            'code': status.HTTP_200_OK,
            'message': 'success',
            'data': serializer.data,
            'error': False
        }
        return Response(result)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            result = {
                'code': status.HTTP_200_OK,
                'message': 'success',
                'data': serializer.data,
                'error': False
            }
            return Response(result)
        else:
            result = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': serializer.errors,
                'data': [],
                'error': True
            }
            return Response(result)