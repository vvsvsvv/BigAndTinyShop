from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('categories/', adminapp.categories, name='categories'),
    path('subcategories/<int:pk>/', adminapp.subcategories, name='subcategories'),
    path('products/<int:category_pk>/<int:subcategory_pk>/', adminapp.products, name='products'),
]
