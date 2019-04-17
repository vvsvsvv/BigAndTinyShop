from django.urls import path, re_path
import authapp.views as auth

app_name = 'authapp'

urlpatterns = [
    path('login/', auth.login, name='login'),
    path('logout/', auth.logout, name='logout'),
    path('register/', auth.register, name='register'),
    path('update/', auth.update, name='update'),
    re_path(r'verify/(?P<email>.+)/(?P<activation_key>\w+)/$', auth.verify, name='verify'),
]
