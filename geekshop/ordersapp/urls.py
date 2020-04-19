from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrdersList.as_view(), name='orders_list'),
    path('create/', ordersapp.OrderCreate.as_view(), name='order_create'),
    path('update/<int:pk>/', ordersapp.OrderUpdate.as_view(), name='order_update'),
    # path('update/<int:pk>/<int:quantity>/', ordersapp.update),
]
