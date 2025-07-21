from django.urls import path
from . import views

app_name = 'pirostagram'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path("comment/create/", views.comment_create_ajax, name='comment_create'),
    path("comment/delete/", views.comment_delete_ajax, name='comment_delete'),
]