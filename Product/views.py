from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import productserializer
from .models import product
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UserSerializer
from django.contrib.auth.models import User

# Create your views here.

'''@api_view(['Get'])
def api_overview(request):
    api_urls={
        'List': '/product-list/',
        'Detail view': '/product-detail/<int:id>',
        'Create': '/product-create/',
        'Update': '/product-update/<int:id>',
        'Delete': '/product-delete/<int:id>',
    }
    return Response(api_urls)  '''


#list
@api_view(['Get'])
def showall(request):
    products = product.objects.all()
    serializer = productserializer(products, many=True)
    return Response(serializer.data)

#single product

@api_view(['Get'])
def Viewproduct(request,pk):
    Product = product.objects.get(id=pk)
    serializer = productserializer(Product, many=False)
    return Response(serializer.data)

#create product
@api_view(['Post'])
def createproduct(request):
    serializer = productserializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#update
@api_view(['Post'])
def Updateproduct(request,pk):
    Products = product.objects.get(id=pk)
    serializer = productserializer(instance=Products, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#delete
@api_view(['Get'])
def Deleteproduct(request,pk):
    Products = product.objects.get(id=pk)
    Products.delete()

    return Response("Items Deleted Successfully")

