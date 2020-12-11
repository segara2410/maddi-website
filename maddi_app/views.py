from django import template
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader

from .decorators import *
from .forms import *
from .models import *
import http.client

# @login_required(login_url="/login/")
def index(request):
  return render(request, 'maddi_app/index.html')

def shop(request):
  items = Item.objects.all()
  return render(request, 'maddi_app/shop.html', {
    'items': items,
  })

def create_item_view(request):
  if request.method == 'POST':
    form = ItemForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('shop')
  else:
    form = ItemForm(None)

  return render(request, 'maddi_app/item/add.html', {
    'form': form,
  })

def retrieve_item_view(request, id):
  item = Item.objects.get(pk=id)
  return render(request, 'maddi_app/item/retrieve.html', {
    'item': item,
  })

def payment(request):
  return render(request, 'maddi_app/payment.html')
  
def journal(request):
  return render(request, 'maddi_app/journal.html')

def about(request):
  return render(request, 'maddi_app/about.html')

def cart(request):
  return render(request, 'maddi_app/cart.html')

@anonymous_required('index')
def login_view(request):
  if request.user.is_authenticated:
      return redirect('index')

  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('index')

    return render(request, 'accounts/login.html', {'form':form})

  form = AuthenticationForm()
  return render(request, 'accounts/login.html', {'form':form})

@anonymous_required('index')
def register_view(request):
  return render(request, 'accounts/register.html')

def logout_view(request):
  logout(request)
  return redirect('/')

def province(request, id=None):
  conn = http.client.HTTPSConnection("api.rajaongkir.com")

  headers = { 'key': "833e8c949f70274cf9632f00c45919a8" }

  if id:
    conn.request("GET", f"/starter/city?province={id}", headers=headers)
  else:
    conn.request("GET", f"/starter/city", headers=headers)

  res = conn.getresponse()
  data = res.read()

  return HttpResponse(data.decode("utf-8"))

def city(request):
  conn = http.client.HTTPSConnection("api.rajaongkir.com")

  headers = { 'key': "833e8c949f70274cf9632f00c45919a8" }

  conn.request("GET", "/starter/city", headers=headers)

  res = conn.getresponse()
  data = res.read()

  return HttpResponse(data.decode("utf-8"))

def cost(request, id):
  conn = http.client.HTTPSConnection("api.rajaongkir.com")

  payload = f"origin=444&destination={id}&weight=1000&courier=jne"

  headers = {
    'key': "833e8c949f70274cf9632f00c45919a8",
    'content-type': "application/x-www-form-urlencoded"
  }

  conn.request("POST", "/starter/cost", payload, headers)

  res = conn.getresponse()
  data = res.read()

  return HttpResponse(data.decode("utf-8"))
