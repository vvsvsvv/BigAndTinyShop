from django.urls import path
import adminapp.views as admin

app_name = 'adminapp'

urlpatterns = [
    path('', admin.index, name='index'),
]
