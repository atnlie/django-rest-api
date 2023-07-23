from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
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
        'error': False
    }
    return Response(result, status=status.HTTP_200_OK)

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
        return Response(result, status=status.HTTP_201_CREATED)
    else:
        result = {
            'code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors,
            'data': [],
            'error': True
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)

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
        return Response(result, status=status.HTTP_200_OK)
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
            return Response(result, status=status.HTTP_400_BAD_REQUEST)


class ProductList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        result = {
            'code': status.HTTP_200_OK,
            'message': 'success',
            'data': serializer.data,
            'error': False
        }
        return Response(result)

    def post(self, request, format=None):
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
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

class ProductDetail(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
            #TODO: return result data empty

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        result = {
            'code': status.HTTP_200_OK,
            'message': 'success',
            'data': serializer.data,
            'error': False
        }
        return Response(result, status=status.HTTP_200_OK) 

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            result = {
                'code': status.HTTP_200_OK,
                'message': 'success',
                'data': serializer.data,
                'error': False
            }
            return Response(result, status=status.HTTP_200_OK)
        else:
            result = {
                'code': status.HTTP_400_BAD_REQUEST,
                'message': serializer.errors,
                'data': [],
                'error': True
            }
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        result = {
            'code': status.HTTP_204_NO_CONTENT,
            'message': 'success',
            'data': [],
            'error': False
        }
        return Response(result, status=status.HTTP_204_NO_CONTENT)