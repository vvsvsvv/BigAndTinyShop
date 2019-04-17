import json

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from mainapp.models import ProductCategory, ProductSubCategory, Product

def upload_db():
    # function for uploading db data to json
    categories = ProductCategory.objects.all()
    categories_list = []

    with open('categories.json', 'w', encoding='utf-8') as categories_json:
        for category in categories:
            categories_list.append(dict(filter(lambda x: not x[0].startswith('_'), category.__dict__.items())))
        json.dump(categories_list, categories_json)


    subcategories = ProductSubCategory.objects.all()
    subcategories_list = []

    with open('subcategories.json', 'w', encoding='utf-8') as subcategories_json:
        for subcategory in subcategories:
            subcategories_list.append(dict(filter(lambda x: not x[0].startswith('_'), subcategory.__dict__.items())))
        json.dump(subcategories_list, subcategories_json)

    products = Product.objects.all()
    product_list = []

    with open('products.json', 'w', encoding='utf-8') as products_json:
        for product in products:
            product_list.append(dict(filter(lambda x: not x[0].startswith('_'), product.__dict__.items())))
        json.dump(product_list, products_json, default=float)



def index(request):
    context = {
        'page_title': 'Big and Tiny - Knitwear for big and tiny people',
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request, category_pk=0, subcategory_pk=0, page=1):

    # upload_db()

    categories_and_subcategories = {category:None for category in ProductCategory.objects.filter(is_active=True)}

    if int(category_pk) == 0:
        products = Product.objects.filter(is_active=True).order_by('price')
    else:
        category = get_object_or_404(ProductCategory, pk=category_pk)
        subcategories = category.productsubcategory_set.filter(is_active=True)
        categories_and_subcategories[category] = subcategories

        if int(subcategory_pk) == 0:
            products = []
            for subcategory in subcategories:
                products.extend(subcategory.product_set.filter(is_active=True))
        else:
            subcategory = get_object_or_404(ProductSubCategory, pk=subcategory_pk)
            products = subcategory.product_set.filter(is_active=True).order_by('price')

    paginator = Paginator(products, 3)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator(num_pages))

    context = {
        'page_title': 'каталог',
        'categories': categories_and_subcategories,
        'category_pk': category_pk,
        'subcategory_pk': subcategory_pk,
        'products': products,
    }

    return render(request, 'mainapp/catalog.html', context)


def product(request, pk):
    title = 'страница продукта'

    context = {
        'page_title': title,
        'object': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/product.html', context)


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