from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from mainapp.models import Product
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from django.urls import reverse


@login_required
def index(request):
    title = 'корзина'
    basket_items = request.user.basket.order_by('product__subcategory')

    context = {
        'title': title,
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/index.html', context)


@login_required
def add(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('main:product',
                                            kwargs={
                                                'pk': pk,
                                            }
                                            ))

    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    # basket = request.user.basket.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    # TODO уменьшать количество товаров в базе
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def remove(request, pk):
    get_object_or_404(Basket, pk=pk).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))