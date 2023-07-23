from django.urls import path
from django.conf import settings
# from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.getProduct, name='getProduct'),
    path('get-all/', views.getAllProducts, name='getAllProduct'),
    path('add-product/', views.addProduct, name='addProduct'),
    path('product/', views.product, name='product'),
    path('product-list/', views.ProductList.as_view(), name='product-list'),
    path('product-list/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
