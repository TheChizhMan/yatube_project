from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index.html'),
    path('group_list/', views.group_list),
    path('posts/', views.group_posts, name='posts_list'),
    path('posts/<str:pk>/', views.group_style)
]

