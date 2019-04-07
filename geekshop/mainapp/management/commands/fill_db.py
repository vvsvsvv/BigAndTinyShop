from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, ProductSubCategory, Product
from authapp.models import ShopUser

import json
import os

JSON_PATH = ''

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        [ProductCategory.objects.create(**category) for category in categories]

        subcategories = load_from_json('subcategories')

        ProductSubCategory.objects.all().delete()
        for subcategory in subcategories:
            category_id = subcategory['category_id']
            # get category by its name
            _category = ProductCategory.objects.get(id=category_id)
            # replace category name with its object
            subcategory['category'] = _category

        [ProductSubCategory.objects.create(**subcategory) for subcategory in subcategories]

        products = load_from_json('products')

        Product.objects.all().delete()
        for product in products:
            subcategory_id = product['subcategory_id']
            # get subcategory by its name
            _subcategory = ProductSubCategory.objects.get(id=subcategory_id)
            # replace subcategory name with its object
            product['subcategory'] = _subcategory

        [Product.objects.create(**product) for product in products]

        # create superuser
        if not ShopUser.objects.filter(username='gjango').exists():
            ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=25)