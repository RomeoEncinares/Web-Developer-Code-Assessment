from .views import index, register, login, home, createArticle, viewArticle
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register_user'),
    path('login/', login, name='login_user'),
    path('home/', home, name='home_user'),
    path('createArticle/', createArticle, name='create_article'),
    path('article/<int:id>/', viewArticle, name='view_article'),
]