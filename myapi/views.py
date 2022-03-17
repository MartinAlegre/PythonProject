from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ProductSerializer , OrderDetailSerializer , OrderSerializer
from .models import Order, OrderDetail, Product
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all().order_by('id_PK')
    serializer_class = ProductSerializer

    def create(self, request):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'producto creado correctamente'})

        return Response({'message':'producto no creado'})

    def update(self, request, pk=None):
        #ProductUpdate
        Product = self.get_object()
        data = request.data
        if data.get("stock",Product.stock) > 0 and data.get("price",Product.price) > 0 :
            Product.id_PK = data.get("id_PK",Product.id_PK)
            Product.name = data.get("name",Product.name)
            Product.price = data.get("price",Product.price)
            Product.stock = data.get("stock",Product.stock)
            Product.save()
            return Response({'message':'Producto Actualizado'})
        else:
            return Response({'message':'ERROR Producto no actualizado'})

    
    def partial_update(self, request,pk=None):
        #stockupdate
        Product = self.get_object()
        data = request.data
        if data.get("stock",Product.stock) > 0:
            Product.stock = data.get("stock",Product.stock)
            Product.save()
            return Response({'message':'Stock Actualizado'})
        else :
            return Response({'message':'ERROR Stock < 0'})
        

class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all().order_by('id_PK')
    serializer_class = OrderSerializer


class OrderDetailViewSet(viewsets.ModelViewSet):

    queryset = OrderDetail.objects.all().order_by('quantity')
    serializer_class = OrderDetailSerializer
    def create(self, request):
        Serializer = self.get_serializer(data = request.data)
        if Serializer.is_valid():
            #Product.reduce_stock(Serializer.data.quantity)
            #wea = Product.objects.get()
            
            return Response(Serializer)
        else:
            return Response({'message':'ERROR Stock < 0'})