from django.shortcuts import render, get_object_or_404
from . import models
from .models import Products


def index(request):
    return render(request, 'pet_shop/index.html')


def shop(request):
    products = Products.objects.all()
    context = {
        'prod': products,
    }
    return render(request, 'pet_shop/shop.html', context)


def product(request, product_id):
    item = get_object_or_404(models.Products, id=product_id)
    # book = models.Book.objects.get(id=book_id)
    # reviews = models.Review.objects.filter(book=book)
    context = {
        "item": item,
    }
    return render(request, "pet_shop/product.html", context)


