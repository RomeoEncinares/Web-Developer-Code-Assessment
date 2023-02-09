from .views import index, register, login, home
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register_user'),
    path('login/', login, name='login_user'),
    path('home/', home, name='home_user'),
]