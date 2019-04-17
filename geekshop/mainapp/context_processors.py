def basket(request):
    print('context processor basket works')
    basket = []

    if request.user.is_authenticated:
        basket = request.user.basket.all().order_by('product__subcategory')

    return {
        'basket': basket,
    }