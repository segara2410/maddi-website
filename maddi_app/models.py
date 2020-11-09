from django.db import models
from django.contrib.auth.models import User
from smartfields import fields

class Customer(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  phone_number = models.CharField(max_length=12)
  address = models.CharField(max_length=250)
  city = models.PositiveIntegerField()
  postal_code = models.IntegerField()

class News(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=40)
  body = models.TextField()
  image = fields.ImageField(upload_to='news')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
  name = models.CharField(max_length=40)

class Item(models.Model):
  name = models.CharField(max_length=40)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  stock = models.IntegerField()
  price = models.IntegerField()
  description = models.TextField()
  image = fields.ImageField(upload_to='item')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Courrier(models.Model):
  name = models.CharField(max_length=40)

class Review(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  description = models.TextField()
  rating = models.FloatField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

class Purchase(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  items = models.ManyToManyField('Item', through='Cart', through_fields=('purchase', 'item'))
  destination_address = models.CharField(max_length=250)
  destination_city = models.PositiveIntegerField()
  cancellation = models.SmallIntegerField()
  created_at = models.DateTimeField(auto_now_add=True)

class Cart(models.Model):
  purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE)
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  message = models.TextField()
  total_price = models.BigIntegerField()

class Shipping(models.Model):
  purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
  status = models.CharField(max_length=20)
  courrier = models.ForeignKey(Courrier, on_delete=models.CASCADE)
  shipping_price = models.BigIntegerField()
  date_shipped = models.DateTimeField()
  date_arrived = models.DateTimeField()

class Payment(models.Model):
  purchase = models.OneToOneField(Purchase, on_delete=models.CASCADE)
  payment_amount = models.BigIntegerField()
  date_paid = models.DateTimeField()
  method = models.CharField(max_length=30)
  status = models.CharField(max_length=30)
  updated_at = models.DateTimeField(auto_now=True)
