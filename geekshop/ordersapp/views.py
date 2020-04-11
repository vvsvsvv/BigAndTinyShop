from django.shortcuts import render
from django.views.generic import ListView
from ordersapp.models import Order


class OrdersList(ListView):
    model = Order
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
