from django.shortcuts import render

def index(request):
    context={
        'page_title': 'Главная'
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request):
    context={
        'page_title': 'Каталог'
    }

    return render(request, 'mainapp/catalog.html', context)


def contacts(request):
    locations = {
        'city': 'Москва',
        'phone': '8(000)000-00-00',
        'address': 'Улица, дом'
    }

    context={
        'page_title': 'Контакты',
        'locations': locations
    }


    return render(request, 'mainapp/contacts.html', context)