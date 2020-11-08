from django.urls import path

from . import views

urlpatterns = [
  path("province/", views.province, name="province"),
  path("province/<int:id>/", views.province, name="province_cities"),
  path("city/", views.city, name="city"),
  path("cost/<int:id>/", views.cost, name="cost"),
]