from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import ShopUser
from mainapp.models import ProductCategory, ProductSubCategory, Product
from adminapp.forms import ShopUserUpdateAdminForm, ShopUserCreationAdminForm, ProductCategoryEditForm, ProductSubCategoryEditForm, ProductEditForm


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

    object_list = subcategory.product_set.all().order_by('-is_active', 'name')

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


def productcategory_create(request):
    title = 'категории/создание'

    if request.method == 'POST':
        form = ProductCategoryEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:categories'))
    else:
        form = ProductCategoryEditForm()

    context = {
        'title': title,
        'form': form
    }

    return render(request, 'adminapp/productcategory_update.html', context)


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


def productcategory_delete(request, pk):
    title = 'категории/удаление'

    object = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        object.is_active = False
        object.save()
        return HttpResponseRedirect(reverse('myadmin:categories'))

    context = {
        'title': title,
        'object': object
    }

    return render(request, 'adminapp/productcategory_delete.html', context)


def productsubcategory_create(request, pk):
    title = 'подкатегории/создание'

    category = get_object_or_404(ProductCategory,pk=pk)
    if request.method == 'POST':
        form = ProductSubCategoryEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:subcategories', kwargs={'pk': pk}))
    else:
        form = ProductSubCategoryEditForm(initial={'category': category})

    context = {
        'title': title,
        'form': form,
        'category': category
    }

    return render(request, 'adminapp/productsubcategory_update.html', context)


def productsubcategory_update(request, category_pk, subcategory_pk):
    title = 'подкатегории/редактирование'

    category = get_object_or_404(ProductCategory,pk=category_pk)
    current_object = get_object_or_404(ProductSubCategory, pk=subcategory_pk)
    if request.method == 'POST':
        form = ProductSubCategoryEditForm(request.POST, request.FILES, instance=current_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:subcategories', kwargs={'pk': category_pk}))
    else:
        form = ProductSubCategoryEditForm(initial={'category': category}, instance=current_object)

    context = {
        'title': title,
        'form': form,
        'category': category
    }

    return render(request, 'adminapp/productsubcategory_update.html', context)


def productsubcategory_delete(request, pk):
    title = 'подкатегории/удаление'

    object = get_object_or_404(ProductSubCategory, pk=pk)

    if request.method == 'POST':
        object.is_active = False
        object.save()
        return HttpResponseRedirect(reverse('myadmin:subcategories', kwargs={'pk': object.category.pk}))

    context = {
        'title': title,
        'object': object
    }

    return render(request, 'adminapp/productsubcategory_delete.html', context)


def product_create(request, category_pk, subcategory_pk):
    title = 'продукты/создание'

    category = get_object_or_404(ProductCategory, pk=category_pk)
    subcategory = get_object_or_404(ProductSubCategory, pk=subcategory_pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:products',
                                                kwargs={
                                                    'category_pk': category_pk,
                                                    'subcategory_pk': subcategory_pk
                                                }))
    else:
        form = ProductEditForm(initial={'subcategory': subcategory})

    context = {
        'title': title,
        'form': form,
        'category': category,
        'subcategory': subcategory
    }

    return render(request, 'adminapp/product_update.html', context)


def product_read(request, pk):
    title = 'продукт/подробнее'

    product_object = get_object_or_404(Product, pk=pk)

    context = {
        'title': title,
        'object': product_object
    }

    return render(request, 'adminapp/product_detail.html', context)


def product_update(request, category_pk, subcategory_pk, product_pk):
    title = 'продукты/редактирование'

    category = get_object_or_404(ProductCategory, pk=category_pk)
    subcategory = get_object_or_404(ProductSubCategory, pk=subcategory_pk)
    current_object = get_object_or_404(Product, pk=product_pk)
    if request.method == 'POST':
        form = ProductEditForm(request.POST, request.FILES, instance=current_object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:products',
                                                kwargs={
                                                    'category_pk': category_pk,
                                                    'subcategory_pk': subcategory_pk
                                                }))
    else:
        form = ProductEditForm(initial={'subcategory': subcategory}, instance=current_object)

    context = {
        'title': title,
        'form': form,
        'category': category,
        'subcategory': subcategory
    }

    return render(request, 'adminapp/product_update.html', context)


def product_delete(request, pk):
    title = 'подкатегории/удаление'

    object = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        object.is_active = False
        object.save()
        return HttpResponseRedirect(reverse('myadmin:products',
                                            kwargs={
                                                'category_pk': object.subcategory.category.pk,
                                                'subcategory_pk': object.subcategory.pk
                                            }))

    context = {
        'title': title,
        'object': object
    }

    return render(request, 'adminapp/product_delete.html', context)