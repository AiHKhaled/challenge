from django.shortcuts import render
from .models import Product
from rest_framework import viewsets
from .serializers import ProductSerializer 
# Create your views here.
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('created_at')
    serializer_class = ProductSerializer