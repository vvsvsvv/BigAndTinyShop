from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('', adminapp.index, name='index'),
    path('categories/', adminapp.categories, name='categories'),
    path('subcategories/<int:pk>/', adminapp.subcategories, name='subcategories'),
    path('products/<int:category_pk>/<int:subcategory_pk>/', adminapp.products, name='products'),

    path('shopuser/create/', adminapp.shopuser_create, name='shopuser_create'),
    path('shopuser/update/<int:pk>/', adminapp.shopuser_update, name='shopuser_update'),
    path('shopuser/delete/<int:pk>/', adminapp.shopuser_delete, name='shopuser_delete'),

    path('productcategory/update/<int:pk>/', adminapp.productcategory_update, name='productcategory_update'),
    path('productsubcategory/update/<int:pk>/', adminapp.productsubcategory_update, name='productsubcategory_update'),


]
