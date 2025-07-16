# ideas/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/edit/', views.idea_edit, name='idea_edit'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('<int:pk>/toggle_star/', views.toggle_star, name='toggle_star'),
    path('<int:pk>/adjust_interest/', views.adjust_interest, name='adjust_interest'),
    path('devtools/create/', views.devtool_create, name='devtool_create'),
    path('devtools/', views.devtool_list, name='devtool_list'),
    path('devtools/<int:pk>/', views.devtool_detail, name='devtool_detail'),
    path('devtools/<int:pk>/edit/', views.devtool_edit, name='devtool_edit'),
    path('devtools/<int:pk>/delete/', views.devtool_delete, name='devtool_delete'),
]