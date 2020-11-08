from django.db import models
from django.contrib.auth.models import User
from smartfields import fields

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=12)
  address = models.CharField(max_length=250)
  city = models.PositiveIntegerField()
  postal_code = models.IntegerField()

class Category(models.Model):
  name = models.CharField(max_length=40)

class Item(models.Model):
  name = models.CharField(max_length=40)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  stock = models.IntegerField()
  price = models.IntegerField()
  description = models.TextField()
  image = fields.ImageField(upload_to='item')
  
class Purchase(models.Model):
  user = models.OneToOneField(Customer, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  destination_address = models.CharField(max_length=250)
  destination_city = models.PositiveIntegerField()
  quantity = models.IntegerField()
  message = models.TextField()
  cancellation = models.SmallIntegerField()

class Shipping(models.Model):
  purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
  status = models.CharField(max_length=20)

class Payment(models.Model):
  purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
  total_price = models.IntegerField()
  date_paid = models.DateTimeField()
  method = models.CharField(max_length=30)
  status = models.CharField(max_length=30)