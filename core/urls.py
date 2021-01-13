from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index),
    path('checkout', views.checkout, name="checkout"),
    path('product', views.product, name='product')


]
