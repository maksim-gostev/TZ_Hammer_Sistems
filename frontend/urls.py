from django.urls import path

from frontend.views import get_or_create_user, userlogin, userdetail

app_name = 'frontend'

urlpatterns = [
    path('', get_or_create_user , name='index'),
    path('auth/<int:pk>/', userlogin, name='login'),
    path('deteil/<int:pk>/', userdetail, name='user'),
]