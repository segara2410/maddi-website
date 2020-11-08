from django.shortcuts import render
from django.http import HttpResponse
import http.client

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