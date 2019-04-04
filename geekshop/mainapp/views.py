from django.shortcuts import render, HttpResponseRedirect
from mainapp.models import ProductCategory, ProductSubCategory, Product
from django.urls import reverse
import json

def upload_db():
    # function for uploading db data to json
    categories = ProductCategory.objects.all()

    with open('categories.json', 'w', encoding='utf-8') as categories_json:
        for category in categories:
            json.dump(dict(filter(lambda x: not x[0].startswith('_'), category.__dict__.items())), categories_json)

    products = Product.objects.all()

    with open('products.json', 'w', encoding='utf-8') as products_json:
        for product in products:
            json.dump(dict(filter(lambda x: not x[0].startswith('_'), product.__dict__.items())), products_json, default=float)

def index(request):
    context={
        'page_title': 'Big and Tiny - Knitwear for big and tiny people'
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request):

    # categories = []

    # upload_db()

    # # Подгрузка изображения первого представителя категории в качестве обложки категории
    # for category in ProductCategory.objects.all():
    #
    #     first_product = Product.objects.filter(category=category)[0]
    #
    #     category_image = first_product.image
    #
    #     setattr(category, 'image', category_image)
    #
    #     categories.append(category)

    categories_and_subcategories = {}

    categories = ProductCategory.objects.all()

    for category in categories:
        categories_and_subcategories[category] = ProductSubCategory.objects.filter(category=category)

    products = Product.objects.all()

    context={
        'page_title': 'каталог',
        'categories': categories_and_subcategories,
        'products': products
    }

    return render(request, 'mainapp/catalog.html', context)


def category(request, pk):
    print(f'выбрано {pk}')
    return HttpResponseRedirect(reverse('main:catalog'))


def contacts(request):

    locations = {
        'city': 'Москва',
        'phone': '8(000)000-00-00',
        'address': 'Улица, дом'
    }

    context={
        'page_title': 'контакты',
        'locations': locations,
    }


    return render(request, 'mainapp/contacts.html', context)