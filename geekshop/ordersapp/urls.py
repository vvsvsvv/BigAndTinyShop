from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrdersList.as_view(), name='orders_list'),
    path('create/', ordersapp.OrderCreate.as_view(), name='order_create'),
    # path('remove/<int:pk>/', ordersapp.remove, name='remove'),
    # path('update/<int:pk>/<int:quantity>/', ordersapp.update),
]
