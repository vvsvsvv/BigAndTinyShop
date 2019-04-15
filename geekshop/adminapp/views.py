from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import ShopUser
from mainapp.models import ProductCategory, ProductSubCategory
from adminapp.forms import ShopUserUpdateAdminForm, ShopUserCreationAdminForm, ProductCategoryEditForm


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    title = 'админка/пользователи'

    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')

    context = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/index.html', context)


@user_passes_test(lambda x: x.is_superuser)
def categories(request):
    title = 'админка/категории'

    object_list = ProductCategory.objects.all().order_by('-is_active', 'name')
    context = {
        'title': title,
        'object_list': object_list
    }
    return render(request, 'adminapp/productcategory_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def subcategories(request, pk):

    category = get_object_or_404(ProductCategory, pk=pk)

    title = f'админка/подкатегории ({category.name})'

    object_list = category.productsubcategory_set.all().order_by('-is_active', 'name')

    context = {
        'title': title,
        'category': category,
        'object_list': object_list
    }
    return render(request, 'adminapp/productsubcategory_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def products(request, category_pk, subcategory_pk):

    category = get_object_or_404(ProductCategory, pk=category_pk)
    subcategory = get_object_or_404(ProductSubCategory, pk=subcategory_pk)

    title = f'админка/товары ({subcategory.name} - {category.name})'

    object_list = subcategory.product_set.all().order_by('name')

    context = {
        'title': title,
        'category': category,
        'subcategory': subcategory,
        'object_list': object_list
    }
    return render(request, 'adminapp/product_list.html', context)


def shopuser_create(request):
    title = 'пользователи/создание'

    if request.method == 'POST':
        form = ShopUserCreationAdminForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserCreationAdminForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/shopuser_update.html', context)


def shopuser_update(request, pk):
    title = 'пользователи/редактирование'

    current_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserUpdateAdminForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserUpdateAdminForm(instance=current_user)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/shopuser_update.html', context)


def shopuser_delete(request, pk):
    title = 'пользователи/удаление'

    object = get_object_or_404(ShopUser, pk=pk)

    if request.method == 'POST':
        # user.delete()
        # вместо удаления делаем неактивным
        object.is_active = False
        object.save()
        return HttpResponseRedirect(reverse('myadmin:index'))

    context = {
        'title': title,
        'user_to_delete': object
    }

    return render(request, 'adminapp/shopuser_delete.html', context)


def productcategory_update(request, pk):
    title = 'категории/редактирование'

    current_object = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES, instance=current_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = ProductCategoryEditForm(instance=current_object)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/productcategory_update.html', context)


def productsubcategory_update(request, pk):
    title = 'категории/редактирование'

    current_object = get_object_or_404(ProductSubCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES, instance=current_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = ProductCategoryEditForm(instance=current_object)

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/productsubcategory_update.html', context)
