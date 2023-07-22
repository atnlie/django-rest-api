from django.urls import path
from . import views
from django.conf import settings
 
urlpatterns = [
    path('', views.getProduct, name='getProduct'),
    path('get-all/', views.getAllProducts, name='getAllProduct'),
    path('add-product/', views.addProduct, name='addProduct'),
]