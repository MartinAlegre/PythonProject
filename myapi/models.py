from http.client import responses
from django.db import models
import requests

class Product(models.Model):
    id_PK = models.CharField(max_length=60, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    price = models.FloatField(max_length=25, blank=True, null=True)
    stock = models.IntegerField(blank=True, null=True)

    def reduce_stock(self,amount,name):
        product = self.objects.all().filter(name)
        product.stock -= amount
        product.save
        return product.stock
    
    def get_product_by_id(self,id):
        product = self.objects.get(id)
        return product
    
    def __str__(self):
        return self.name

class Order(models.Model):
    id_PK = models.CharField(max_length=60, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)

    def get_total(self,request):
        data = request.data
        total = data.quantity*data.value
        return total

    def get_total_usd(self,request):
        response = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
        data = response.json()
        for i in data:
            if data[i].nombre == "dolar blue":
                price = data[i].venta
        data = request.data
        usdtotal = data.quantity*data.value
        usdtotal*price
        return usdtotal

    def __str__(self):
        return self.id_PK

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
