from django.urls import path

from users import views

app_name = 'users_api'

urlpatterns = [
    path('create/', views.UserGetCreat.as_view(), name='user_create'),
    path('auth/<int:pk>/', views.UserLogin.as_view(), name='auth'),
    path('user/<int:pk>/', views.UserGetUpdate.as_view(), name='user_get_update'),
]