from django.shortcuts import render
from .models import ProductCategory, Product


def main(request):
    return render(request, 'mainapp/index.html')


def products(request):
    title = 'Товары'
    product = Product.objects.all()

    content = {'title': title, 'products': product}

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')
