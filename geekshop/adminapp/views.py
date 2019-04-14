from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from mainapp.models import ProductCategory, ProductSubCategory


def index(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/index.html', context)


def categories(request):
    title = 'админка/категории'

    object_list = ProductCategory.objects.all()
    context = {
        'title': title,
        'object_list': object_list
    }
    return render(request, 'adminapp/productcategory_list.html', context)


def subcategories(request, pk):

    category = get_object_or_404(ProductCategory, pk=pk)

    title = f'админка/подкатегории ({category.name})'

    object_list = ProductSubCategory.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': title,
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/productsubcategory_list.html', context)