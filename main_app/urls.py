from knox import views as knox_views
from .views import RegisterAPI, LoginAPI, postArticle, getArticle, updateArticle, getSpecificArticle
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/create-article/', postArticle, name="postArticle"),
    path('api/list-article/', getArticle, name="getArticle"),
    path('api/article/<int:id>/', getSpecificArticle, name='get-specific-article'),
    path('api/update-article/<int:id>/', updateArticle, name="updateArticle"),
]