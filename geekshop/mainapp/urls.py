from django.urls import path
import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp.index, name='index'),

    path('catalog/<int:category_pk>/<int:subcategory_pk>/', mainapp.catalog, name='catalog'),

    path('contacts/', mainapp.contacts, name='contacts'),
]
