from django.urls import path
import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    # path('', adminapp.index, name='index'),
    path('', adminapp.UsersListView.as_view(), name='index'),
    path('categories/', adminapp.categories, name='categories'),
    path('subcategories/<int:pk>/', adminapp.subcategories, name='subcategories'),
    path('products/<int:category_pk>/<int:subcategory_pk>/', adminapp.products, name='products'),

    path('shopuser/create/', adminapp.shopuser_create, name='shopuser_create'),
    path('shopuser/update/<int:pk>/', adminapp.shopuser_update, name='shopuser_update'),
    path('shopuser/delete/<int:pk>/', adminapp.shopuser_delete, name='shopuser_delete'),

    path('productcategory/create/', adminapp.productcategory_create, name='productcategory_create'),
    path('productcategory/update/<int:pk>/', adminapp.productcategory_update, name='productcategory_update'),
    path('productcategory/delete/<int:pk>/', adminapp.productcategory_delete, name='productcategory_delete'),

    path('productsubcategory/create/<int:pk>/', adminapp.productsubcategory_create, name='productsubcategory_create'),
    path('productsubcategory/update/<int:category_pk>/<int:subcategory_pk>/', adminapp.productsubcategory_update, name='productsubcategory_update'),
    path('productsubcategory/delete/<int:pk>/', adminapp.productsubcategory_delete, name='productsubcategory_delete'),

    path('product/create/<int:category_pk>/<int:subcategory_pk>/', adminapp.product_create, name='product_create'),
    path('product/read/<int:pk>/', adminapp.product_read, name='product_read'),
    path('product/update/<int:category_pk>/<int:subcategory_pk>/<int:product_pk>/', adminapp.product_update, name='product_update'),
    path('product/delete/<int:pk>/', adminapp.product_delete, name='product_delete'),
]
