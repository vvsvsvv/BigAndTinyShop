from django.urls import path
import ordersapp.views as ordersapp

app_name = 'ordersapp'

urlpatterns = [
    path('', ordersapp.OrdersList.as_view(), name='orders_list'),
    # path('add/<int:pk>/', ordersapp.add, name='add'),
    # path('remove/<int:pk>/', ordersapp.remove, name='remove'),
    # path('update/<int:pk>/<int:quantity>/', ordersapp.update),
]
