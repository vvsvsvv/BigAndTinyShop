from django.shortcuts import render
import datetime

def index(request):
    context={
        'page_title': 'клавная'
    }

    return render(request, 'mainapp/index.html', context)


def catalog(request):
    context={
        'page_title': 'каталог'
    }

    return render(request, 'mainapp/catalog.html', context)


def contacts(request):

    today = {
        'datetime': datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M")
    }

    locations = {
        'city': 'Москва',
        'phone': '8(000)000-00-00',
        'address': 'Улица, дом'
    }

    context={
        'page_title': 'контакты',
        'locations': locations,
        'datetime': today
    }


    return render(request, 'mainapp/contacts.html', context)