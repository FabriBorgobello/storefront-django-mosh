from django.shortcuts import render
from store.models import Product


def say_hello(request):
    product = Product.objects.filter(unit_price__gte=10).first()

    return render(request, 'hello.html', {'name': 'Fabri', 'product': product})
