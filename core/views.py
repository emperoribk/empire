from django.shortcuts import render
from .models import Item


def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "home-page.html", context)


def checkout(request):
    return render(request, 'checkout-page.html')


def product(request):
    return render(request, 'product-page.html')
